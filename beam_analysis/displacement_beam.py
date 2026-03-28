import numpy as np

from beam_analysis.fem_data_beam import fem_data_beam


def displacement_beam(displacements, mesh_x):
    # Reference finite-element data required to reconstruct the beam geometry.
    (
        element_count,
        _equation_count,
        _node_count,
        _young_modulus,
        _area,
        _izz,
        _height,
        coordinates,
        dof_map,
        connectivity,
    ) = fem_data_beam()

    # Coordinates of the original mesh and of the displaced mesh sampled along each element.
    x_initial = np.zeros((mesh_x + 1, element_count))
    y_initial = np.zeros((mesh_x + 1, element_count))
    x_displacement_global = np.zeros((mesh_x + 1, element_count))
    y_displacement_global = np.zeros((mesh_x + 1, element_count))
    displacement_norm = np.zeros((mesh_x + 1, element_count))

    max_displacement = 0.0
    x_deformed = x_initial.copy()
    y_deformed = y_initial.copy()

    for element_index in range(element_count):
        # End nodes of the current element in zero-based indexing.
        node_1 = connectivity[0, element_index] - 1
        node_2 = connectivity[1, element_index] - 1

        x_1 = coordinates[0, node_1]
        y_1 = coordinates[1, node_1]
        x_2 = coordinates[0, node_2]
        y_2 = coordinates[1, node_2]

        # Element length and orientation in the global basis.
        element_length = np.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)
        cosine = (x_2 - x_1) / element_length
        sine = (y_2 - y_1) / element_length

        # Rotation matrix from global DOFs to local beam DOFs.
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

        # Connectivity vector lm mapping local element DOFs to the reduced global solution.
        local_to_global_dofs = np.zeros(3 * connectivity.shape[0], dtype=int)
        for local_node in range(connectivity.shape[0]):
            global_node = connectivity[local_node, element_index] - 1
            local_to_global_dofs[3 * local_node] = dof_map[0, global_node]
            local_to_global_dofs[3 * local_node + 1] = dof_map[1, global_node]
            local_to_global_dofs[3 * local_node + 2] = dof_map[2, global_node]

        # Nodal displacements of the current element extracted from the global vector U.
        element_displacements_global = np.zeros(len(local_to_global_dofs))
        for dof_index, equation_index in enumerate(local_to_global_dofs):
            if equation_index > 0:
                element_displacements_global[dof_index] = displacements[equation_index - 1]

        element_displacements_local = rotation_matrix @ element_displacements_global

        # Element interpolation is evaluated in the natural coordinate xi in [-1, 1].
        natural_coordinate = -1.0
        natural_coordinate_step = 2.0 / mesh_x

        for column in range(mesh_x + 1):
            # Straight-line interpolation of the undeformed axis in the global basis.
            x_initial[column, element_index] = x_1 * 0.5 * (1.0 - natural_coordinate) + x_2 * 0.5 * (
                1.0 + natural_coordinate
            )
            y_initial[column, element_index] = y_1 * 0.5 * (1.0 - natural_coordinate) + y_2 * 0.5 * (
                1.0 + natural_coordinate
            )

            # Linear axial interpolation of u(x) in the local beam axis.
            local_axial_displacement = element_displacements_local[0] * 0.5 * (
                1.0 - natural_coordinate
            ) + element_displacements_local[3] * 0.5 * (1.0 + natural_coordinate)

            # Hermite shape functions for the transverse displacement field v(x).
            transverse_shape_functions = np.zeros(4)
            transverse_shape_functions[0] = 0.25 * (1.0 - natural_coordinate) ** 2 * (
                2.0 + natural_coordinate
            )
            transverse_shape_functions[1] = (
                element_length
                * (1.0 - natural_coordinate) ** 2
                * (1.0 + natural_coordinate)
                / 8.0
            )
            transverse_shape_functions[2] = 0.25 * (1.0 + natural_coordinate) ** 2 * (
                2.0 - natural_coordinate
            )
            transverse_shape_functions[3] = -(
                element_length
                * (1.0 + natural_coordinate) ** 2
                * (1.0 - natural_coordinate)
                / 8.0
            )

            # Local transverse displacement reconstructed from nodal values and rotations.
            local_transverse_displacement = (
                element_displacements_local[1] * transverse_shape_functions[0]
                + element_displacements_local[2] * transverse_shape_functions[1]
                + element_displacements_local[4] * transverse_shape_functions[2]
                + element_displacements_local[5] * transverse_shape_functions[3]
            )

            # Projection of the local displacement field back to the global basis.
            x_displacement_global[column, element_index] = (
                cosine * local_axial_displacement - sine * local_transverse_displacement
            )
            y_displacement_global[column, element_index] = (
                sine * local_axial_displacement + cosine * local_transverse_displacement
            )

            natural_coordinate += natural_coordinate_step

        # Euclidean norm of the displacement vector at each sampling point.
        displacement_norm[:, element_index] = np.sqrt(
            x_displacement_global[:, element_index] ** 2
            + y_displacement_global[:, element_index] ** 2
        )
        max_displacement = np.max(displacement_norm)

        # Amplification factor used only for graphical visualization of the deformed mesh.
        deformation_scale = 1000.0 * max_displacement
        x_deformed = x_initial + deformation_scale * x_displacement_global
        y_deformed = y_initial + deformation_scale * y_displacement_global

    return max_displacement, x_deformed, y_deformed, x_initial, y_initial
