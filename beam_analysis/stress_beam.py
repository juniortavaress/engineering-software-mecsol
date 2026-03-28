import numpy as np

from beam_analysis.fem_data_beam import fem_data_beam


def stress_beam(displacements, element_index, mesh_x, mesh_y):
    # Reference finite-element data required to reconstruct the kinematics of one element.
    (
        _element_count,
        _equation_count,
        _node_count,
        young_modulus,
        area,
        izz,
        height,
        coordinates,
        dof_map,
        connectivity,
    ) = fem_data_beam()

    # End nodes of the current element in zero-based indexing.
    node_1 = connectivity[0, element_index] - 1
    node_2 = connectivity[1, element_index] - 1

    # Coordinates of the two element nodes in the global basis.
    x_1 = coordinates[0, node_1]
    y_1 = coordinates[1, node_1]
    x_2 = coordinates[0, node_2]
    y_2 = coordinates[1, node_2]

    # Element length and direction cosines defining the local basis orientation.
    element_length = np.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)
    cosine = (x_2 - x_1) / element_length
    sine = (y_2 - y_1) / element_length

    # Rotation operator used to map the nodal displacement vector from the global
    # structural basis to the local beam basis.
    rotation_matrix = np.zeros((6, 6))
    rotation_matrix[0, 0] = cosine
    rotation_matrix[0, 1] = sine
    rotation_matrix[1, 0] = -sine
    rotation_matrix[1, 1] = cosine
    rotation_matrix[2, 2] = 1.0
    rotation_matrix[3, 3] = cosine
    rotation_matrix[3, 4] = sine
    rotation_matrix[4, 3] = -sine
    rotation_matrix[4, 4] = cosine
    rotation_matrix[5, 5] = 1.0

    # Connectivity vector lm mapping the six local DOFs of the beam element to
    # the reduced global displacement vector.
    local_to_global_dofs = np.zeros(3 * connectivity.shape[0], dtype=int)
    for local_node in range(connectivity.shape[0]):
        global_node = connectivity[local_node, element_index] - 1
        local_to_global_dofs[3 * local_node] = dof_map[0, global_node]
        local_to_global_dofs[3 * local_node + 1] = dof_map[1, global_node]
        local_to_global_dofs[3 * local_node + 2] = dof_map[2, global_node]

    # Element nodal displacement vector extracted from the global solution.
    element_displacements_global = np.zeros(len(local_to_global_dofs))
    for dof_index, equation_index in enumerate(local_to_global_dofs):
        if equation_index > 0:
            element_displacements_global[dof_index] = displacements[equation_index - 1]

    # Same displacement vector expressed in the local beam basis.
    element_displacements_local = rotation_matrix @ element_displacements_global

    # Sampling grid in the natural coordinate and through the section height.
    natural_coordinate = -1.0
    natural_coordinate_step = 2.0 / mesh_x
    thickness_step = height / mesh_y
    y_coordinate = -height / 2.0

    y_values = np.zeros(mesh_y + 1)
    x_values = np.zeros(mesh_x + 1)

    for row in range(mesh_y + 1):
        y_values[row] = y_coordinate
        y_coordinate += thickness_step

    # Internal force resultants reconstructed along the beam axis.
    axial_force = np.zeros(mesh_x + 1)
    bending_moment = np.zeros(mesh_x + 1)
    shear_force = np.zeros(mesh_x + 1)

    # Von Mises stress field sampled on the (x, y) grid of the section sweep.
    von_mises_stress = np.zeros((mesh_x + 1, mesh_y + 1))

    for column in range(mesh_x + 1):
        x_values[column] = (1.0 + natural_coordinate) * element_length / 2.0

        # Axial strain-displacement operator B_u and corresponding normal force N(x).
        axial_strain_operator = np.array(
            [-1.0 / element_length, 0.0, 0.0, 1.0 / element_length, 0.0, 0.0]
        )
        axial_strain = axial_strain_operator @ element_displacements_local
        axial_force[column] = young_modulus * area * axial_strain

        # Curvature operator associated with the Hermite interpolation of v(x).
        curvature_operator = np.array(
            [
                0.0,
                (4.0 / element_length**2) * 1.5 * natural_coordinate,
                (4.0 / element_length**2)
                * (0.75 * element_length * natural_coordinate - 0.25 * element_length),
                0.0,
                -(4.0 / element_length**2) * 1.5 * natural_coordinate,
                (4.0 / element_length**2)
                * (0.75 * element_length * natural_coordinate + 0.25 * element_length),
            ]
        )
        curvature = curvature_operator @ element_displacements_local
        bending_moment[column] = young_modulus * izz * curvature

        # Shear-force operator obtained from the beam constitutive relation.
        shear_operator = np.array(
            [
                0.0,
                (8.0 * young_modulus * izz * 1.5) / element_length**3,
                (8.0 * young_modulus * izz * 0.75) / element_length**2,
                0.0,
                -(8.0 * young_modulus * izz * 1.5) / element_length**3,
                (8.0 * young_modulus * izz * 0.75) / element_length**2,
            ]
        )
        shear_force[column] = shear_operator @ element_displacements_local

        for row in range(mesh_y + 1):
            y_coordinate = y_values[row]

            # Normal stress sigma_xx due to the combined axial force and bending moment.
            normal_stress = axial_force[column] / area - bending_moment[column] * y_coordinate / izz

            # Shear stress sigma_xy from the parabolic distribution of a rectangular section.
            shear_stress = (shear_force[column] / (2.0 * izz)) * (
                0.25 * height**2 - y_coordinate**2
            )

            # Principal stresses of the plane-stress state (sigma_xx, sigma_xy).
            principal_stress_1 = 0.5 * normal_stress + 0.5 * np.sqrt(
                normal_stress**2 + 4.0 * shear_stress**2
            )
            principal_stress_2 = 0.5 * normal_stress - 0.5 * np.sqrt(
                normal_stress**2 + 4.0 * shear_stress**2
            )
            principal_stress_3 = 0.0

            # Von Mises equivalent stress used to evaluate the element critical section.
            von_mises_stress[column, row] = np.sqrt(
                (principal_stress_1 - principal_stress_2) ** 2
                + (principal_stress_1 - principal_stress_3) ** 2
                + (principal_stress_2 - principal_stress_3) ** 2
            ) / np.sqrt(2.0)

        natural_coordinate += natural_coordinate_step

    return x_values, y_values, von_mises_stress, axial_force, bending_moment, shear_force
