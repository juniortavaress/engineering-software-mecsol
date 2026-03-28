import numpy as np


def stiff_beam(young_modulus, length, area, izz, c, s):
    # Local Euler-Bernoulli beam stiffness matrix. The axial block depends on EA/L
    # and the flexural block depends on EI/L^3, EI/L^2 and EI/L.
    local_stiffness = np.zeros((6, 6))
    local_stiffness[0, 0] = (area * young_modulus) / length
    local_stiffness[0, 3] = -((area * young_modulus) / length)
    local_stiffness[3, 0] = -((area * young_modulus) / length)
    local_stiffness[3, 3] = (area * young_modulus) / length

    local_stiffness[1, 1] = (12.0 * young_modulus * izz) / (length**3)
    local_stiffness[1, 2] = (6.0 * young_modulus * izz) / (length**2)
    local_stiffness[1, 4] = -((12.0 * young_modulus * izz) / (length**3))
    local_stiffness[1, 5] = (6.0 * young_modulus * izz) / (length**2)

    local_stiffness[2, 1] = (6.0 * young_modulus * izz) / (length**2)
    local_stiffness[2, 2] = (4.0 * young_modulus * izz) / length
    local_stiffness[2, 4] = -((6.0 * young_modulus * izz) / (length**2))
    local_stiffness[2, 5] = (2.0 * young_modulus * izz) / length

    local_stiffness[4, 1] = -((12.0 * young_modulus * izz) / (length**3))
    local_stiffness[4, 2] = -((6.0 * young_modulus * izz) / (length**2))
    local_stiffness[4, 4] = (12.0 * young_modulus * izz) / (length**3)
    local_stiffness[4, 5] = -((6.0 * young_modulus * izz) / (length**2))

    local_stiffness[5, 1] = (6.0 * young_modulus * izz) / (length**2)
    local_stiffness[5, 2] = (2.0 * young_modulus * izz) / length
    local_stiffness[5, 4] = -((6.0 * young_modulus * izz) / (length**2))
    local_stiffness[5, 5] = (4.0 * young_modulus * izz) / length

    # Orthogonal transformation from local element coordinates to global coordinates.
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

    # Similarity transformation K_global = R^T * K_local * R.
    return rotation_matrix.T @ (local_stiffness @ rotation_matrix)
