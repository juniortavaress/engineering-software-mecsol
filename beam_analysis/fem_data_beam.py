import numpy as np


def fem_data_beam():
    # Total number of beam elements in the finite-element mesh.
    element_count = 17

    # Total number of structural nodes.
    node_count = 10

    # Number of active equations after boundary conditions are imposed.
    equation_count = 27

    # Material and cross-section properties used by every element.
    young_modulus = 210e9
    width = 0.02
    height = 0.0729
    area = width * height
    izz = (width * height**3) / 12.0

    # Global nodal coordinates. Each line stores the (x, y) position of one node.
    coordinates = np.array(
        [
            [0.0, 0.0],
            [2.0, 0.0],
            [4.0, 0.0],
            [6.0, 0.0],
            [8.0, 0.0],
            [10.0, 0.0],
            [2.0, 3.0],
            [4.0, 4.0],
            [6.0, 4.0],
            [8.0, 3.0],
        ]
    )

    # Equation numbering matrix for the nodal DOFs (u, v, theta). Zero means a
    # restrained DOF removed from the reduced linear system.
    dof_map = np.array(
        [
            [1, 0, 2],
            [3, 4, 5],
            [6, 7, 8],
            [9, 10, 11],
            [12, 13, 14],
            [0, 0, 15],
            [16, 17, 18],
            [19, 20, 21],
            [22, 23, 24],
            [25, 26, 27],
        ],
        dtype=int,
    )

    # Element connectivity with 1-based node indexing, matching the original
    # implementation used throughout the solver and post-processing stages.
    connectivity = np.array(
        [
            [1, 2],
            [2, 3],
            [3, 4],
            [4, 5],
            [5, 6],
            [6, 10],
            [9, 10],
            [8, 9],
            [7, 8],
            [1, 7],
            [2, 7],
            [3, 7],
            [3, 8],
            [3, 9],
            [4, 9],
            [5, 9],
            [5, 10],
        ],
        dtype=int,
    )

    # Arrays are transposed to preserve the [component, index] convention used
    # by the existing graphing and element routines.
    return (
        element_count,
        equation_count,
        node_count,
        young_modulus,
        area,
        izz,
        height,
        coordinates.T,
        dof_map.T,
        connectivity.T,
    )
