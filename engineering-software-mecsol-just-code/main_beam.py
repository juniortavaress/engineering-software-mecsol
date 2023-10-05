import numpy as np
import matplotlib.pyplot as plt
from fem_data_beam import Fem_data_beam
from stiff_beam import stiff_beam
from distload_beam import distload_beam
from Stress_beam import stress_beam
from Displacement_beam import Displacement_beam

# Limpa a janela de comando
import os

#Para controlar aviso de plots do matplotlib
plt.rcParams['figure.max_open_warning'] = 100

# Define a precisão para double
np.set_printoptions(precision=15)

# Definição do vetor (ou escalar) de parâmetros do elemento
z = 0.0

# Definição da densidade do material (ro)
ro = 7800.0

# Definição da aceleração da gravidade g=(gx,gy) componentes do vetor aceleração gravitacional.
gx = 0.0
gy = -9.81

# Ler dados do problema de elementos finitos
nume, neq, numnp, ee, area, Izz, h, coord, id, no = Fem_data_beam(z)

# Inicialização e determinação da matriz de rigidez global
kk = np.zeros((neq, neq))
F = np.zeros(neq)

# Determinação da matriz de rigidez da estrutura
for n in range(nume):  # Loop sobre todos os elementos finitos

    # Obtenção da incidência nodal do n-ésimo elemento
    i1 = no[0, n] -1
    i2 = no[1, n] -1

    # Obtenção das coordenadas dos nós do n-ésimo elemento
    x1 = coord[0, i1]
    y1 = coord[1, i1]
    x2 = coord[0, i2]
    y2 = coord[1, i2]

    # Determinação do comprimento do n-ésimo elemento (treliça)
    length = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    # Determinação do cosseno e seno do ângulo entre a barra e o eixo x global
    c = (x2 - x1) / length
    s = (y2 - y1) / length

    # Determinação da matriz de rigidez do n-ésimo elemento
    kke = stiff_beam(ee, length, area, Izz, c, s)

    # Determinação do vetor força nodal equivalente
    fe = distload_beam(ro, gx, gy, length, area, Izz, c, s)

    # Construção do vetor de conectividade do elemento
    nodes = no.shape[0]
    lm = np.zeros(nodes * 3)
    for ii in range(nodes):
        in_ = no[ii, n]-1
        lm[3 * ii] = id[0, in_]
        lm[3 * ii + 1] = id[1, in_]
        lm[3 * ii + 2] = id[2, in_]

    # Operador montagem da matriz de rigidez do elemento na matriz de rigidez global
    ns = len(lm)
    for i in range(ns):
        ii = int(lm[i])
        if ii > 0:
            F[ii - 1] += fe[i]
            for j in range(ns):
                jj = int(lm[j])
                if jj > 0:
                    kk[ii - 1, jj - 1] += kke[i, j]

# Determinação do vetor de força global
no_P = 5  # Definição do nó em que está aplicada a carga P
dir_P = 2  # Definição da direção em que está aplicada a carga P, x=1, y=2, z=3.
P = -780000.0  # Definição do valor da carga P aplicada
ii_P = id[dir_P - 1, no_P - 1]
F[ii_P - 1] += P

# Determinação do vetor de deslocamentos nodais
U = np.linalg.solve(kk, F)

# Impressão dos deslocamentos nodais
print("Nodal displacements and rotations:\n", U)
print("")

# Determinação das tensões em cada viga-barra
mx = 40  # Número de partições do intervalo [0, length]
my = mx  # Número de partições do intervalo [-h/2, h/2]

# Inicialização do vetor que contém a tensão equivalente de von Mises máxima em cada elemento
sig_eq_max = np.zeros(nume)

# Posprocessamento para calcular as tensões equivalentes de von Mises em cada elemento
for n in range(nume):  # Loop sobre todos os elementos finitos

    xx, yy, sig, Nex, Mex, Vex = stress_beam(U, z, n+1, mx, my)

    #Plot de gráficos aqui
    plt.figure(num=f'Diagrama do esforço normal do elemento {n+1}')
    plt.plot(xx, Nex)
    plt.xlabel('X')
    plt.ylabel('N(x) - Esforço normal do elemento')
    #plt.title(f'Diagrama do esforço normal do elemento {n+1}')

    # Plot do diagrama de esforço cortante do n-ésimo elemento
    plt.figure(num=f'Diagrama do esforço cortante do elemento {n+1}')
    plt.plot(xx, Vex)
    plt.xlabel('X')
    plt.ylabel('V(x) - Esforço cortante do elemento')
    #plt.title(f'Diagrama do esforço cortante do elemento {n+1}')

    # Plot do diagrama de momento fletor do n-ésimo elemento
    plt.figure(num=f'Diagrama do momento fletor do elemento {n+1}')
    plt.plot(xx, Mex)
    plt.xlabel('X')
    plt.ylabel('M(x) - Momento fletor do elemento')
    #plt.title(f'Diagrama do momento fletor do elemento {n+1}')

    # Plot da distribuição da tensão equivalente de von Mises do n-ésimo elemento
    plt.figure(num=f'Distribuição da tensão equivalente de von Mises {n+1}')
    ax = plt.axes(projection='3d')
    X, Y = np.meshgrid(xx, yy)
    surf = ax.plot_surface(X, Y, sig, cmap='jet', vmin=np.nanmin(sig), vmax=np.nanmax(sig))
    ax.view_init(elev=30, azim=45)  # Ajuste os ângulos elevação (elev) e azimutal (azim) como desejado
    ax.azim = -135  # Ajuste o ângulo azimutal
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('SIG')

    
#######################################################################################################################################



    # Determinação do valor máximo da tensão equivalente de von Mises no n-ésimo elemento
    SigMax = np.max(sig)
    sig_eq_max[n] = SigMax

    # Impressão do valor máximo da tensão equivalente de von Mises para o n-ésimo elemento
    print(f"Tensão equivalente de von Mises máxima no elemento {n+1} =", SigMax)


# Impressão da tensão equivalente de von Mises máxima em toda a estrutura
SigMaxMax = np.max(sig_eq_max)
print("")
print("A tensão equivalente máxima de von Mises em toda a estrutura =", SigMaxMax)


# Cálculo das magnitudes máximas de deslocamento em cada elemento e na estrutura
z1 = Displacement_beam(U, z, mx)



# Exibição dos gráficos
plt.show()
