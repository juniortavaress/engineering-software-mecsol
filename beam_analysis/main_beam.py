import numpy as np

from beam_analysis.distload_beam import distload_beam
from beam_analysis.stiff_beam import stiff_beam


class MainBeam:
    @staticmethod
    def solve_structure(
        element_count,
        equation_count,
        young_modulus,
        area,
        izz,
        coordinates,
        dof_map,
        connectivity,
        applied_load,
        loaded_node,
        loaded_direction,
    ):
        # Numerical precision is relevant here because the stiffness assembly and
        # the linear solve propagate rounding errors to the stress post-processing.
        np.set_printoptions(precision=15)

        # Scalar parameter passed to legacy post-processing routines.
        z = 0.0

        # Material density and gravitational acceleration used to build the
        # consistent self-weight load vector of each beam element.
        density = 7800.0
        gravity_x = 0.0
        gravity_y = -9.81

        # Global stiffness matrix K and global load vector F of the reduced system.
        global_stiffness = np.zeros((equation_count, equation_count))
        global_force = np.zeros(equation_count)

        # Element-by-element assembly of K and F.
        for element_index in range(element_count):
            # Nodal incidence of the current beam element in 1-based numbering.
            node_1 = connectivity[0, element_index] - 1
            node_2 = connectivity[1, element_index] - 1

            # Global coordinates of the two element nodes.
            x_1 = coordinates[0, node_1]
            y_1 = coordinates[1, node_1]
            x_2 = coordinates[0, node_2]
            y_2 = coordinates[1, node_2]

            # Element geometry and orientation with respect to the global axes.
            element_length = np.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)
            cosine = (x_2 - x_1) / element_length
            sine = (y_2 - y_1) / element_length

            # Local element contributions projected to the global reference frame.
            element_stiffness = stiff_beam(
                young_modulus, element_length, area, izz, cosine, sine
            )
            element_load = distload_beam(
                density, gravity_x, gravity_y, element_length, area, cosine, sine
            )

            # Connectivity vector lm mapping local DOFs to the reduced global system.
            local_to_global_dofs = np.zeros(connectivity.shape[0] * 3, dtype=int)
            for local_node in range(connectivity.shape[0]):
                global_node = connectivity[local_node, element_index] - 1
                local_to_global_dofs[3 * local_node] = dof_map[0, global_node]
                local_to_global_dofs[3 * local_node + 1] = dof_map[1, global_node]
                local_to_global_dofs[3 * local_node + 2] = dof_map[2, global_node]

            # Standard finite-element assembly operator.
            for row_index, equation_row in enumerate(local_to_global_dofs):
                if equation_row <= 0:
                    continue

                global_force[equation_row - 1] += element_load[row_index]

                for column_index, equation_column in enumerate(local_to_global_dofs):
                    if equation_column <= 0:
                        continue

                    global_stiffness[equation_row - 1, equation_column - 1] += (
                        element_stiffness[row_index, column_index]
                    )

        # External concentrated load applied to one active degree of freedom.
        load_equation = dof_map[loaded_direction - 1, loaded_node - 1]
        global_force[load_equation - 1] += applied_load

        # Linear system K * U = F for nodal displacements and rotations.
        displacements = np.linalg.solve(global_stiffness, global_force)

        # Sampling density adopted by the stress and deformation reconstruction.
        mesh_x = 40
        mesh_y = mesh_x

        # Post-processing buffer storing the maximum Von Mises stress per element.
        equivalent_stress_max = np.zeros(element_count)

        return displacements, z, mesh_x, mesh_y, equivalent_stress_max
