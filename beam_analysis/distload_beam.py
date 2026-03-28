import numpy as np


def distload_beam(ro, gx, gy, length, area, c, s):
    # Equivalent nodal load vector associated with the element self-weight in the
    # local beam basis. The axial terms come from gx and the transverse terms from gy.
    local_equivalent_load = np.zeros(6)
    local_equivalent_load[0] = 0.5 * ro * area * gx * length
    local_equivalent_load[1] = 0.5 * ro * area * gy * length
    local_equivalent_load[2] = (ro * area * gy * length**2) / 12.0
    local_equivalent_load[3] = 0.5 * ro * area * gx * length
    local_equivalent_load[4] = 0.5 * ro * area * gy * length
    local_equivalent_load[5] = -(ro * area * gy * length**2) / 12.0

    # Rotation operator between the local element basis and the global structural basis.
    rotation_matrix = np.zeros((6, 6))
    rotation_matrix[0, 0] = c
    rotation_matrix[0, 1] = s
    rotation_matrix[1, 0] = -s
    rotation_matrix[1, 1] = c
    rotation_matrix[2, 2] = 1.0
    rotation_matrix[3, 3] = c
    rotation_matrix[3, 4] = s
    rotation_matrix[4, 3] = -s
    rotation_matrix[4, 4] = c
    rotation_matrix[5, 5] = 1.0

    # Projection of the consistent load vector to the global assembly basis.
    return rotation_matrix.T @ local_equivalent_load
