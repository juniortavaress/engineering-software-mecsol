import numpy as np
#import matplotlib.pyplot as plt
from calculationsCodes.stiff_beam import stiff_beam
from calculationsCodes.distload_beam import distload_beam
from calculationsCodes.Stress_beam import stress_beam
from calculationsCodes.Displacement_beam import Displacement_beam

# Limpa a janela de comando
import os


class MainBeam():
    def __init__(self):
        super(MainBeam, self).__init__()

    def grafico(self, nume, neq, numnp, ee, area, Izz, h, coord, id, no, P, no_P, dir_P):
        print(coord, id, no)
        #Para controlar aviso de plots do matplotlib
#        plt.rcParams['figure.max_open_warning'] = 100

        # Define a precisão para double
        np.set_printoptions(precision=15)

        # Definição do vetor (ou escalar) de parâmetros do elemento
        z = 0.0

        # Definição da densidade do material (ro)
        ro = 7800.0

        # Definição da aceleração da gravidade g=(gx,gy) componentes do vetor aceleração gravitacional.
        gx = 0.0
        gy = -9.81


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
        #no_P = 5  # Definição do nó em que está aplicada a carga P
        #dir_P = 2  # Definição da direção em que está aplicada a carga P, x=1, y=2, z=3.
        #P = -780000.0  # Definição do valor da carga P aplicada
        ii_P = id[dir_P - 1, no_P - 1]
        F[ii_P - 1] += P

        # Determinação do vetor de deslocamentos nodais
        U = np.linalg.solve(kk, F)

        # Impressão dos deslocamentos nodais
        #print("Nodal displacements and rotations:\n", U)
        #print("")

        # Determinação das tensões em cada viga-barra
        mx = 40  # Número de partições do intervalo [0, length]
        my = mx  # Número de partições do intervalo [-h/2, h/2]

        # Inicialização do vetor que contém a tensão equivalente de von Mises máxima em cada elemento
        sig_eq_max = np.zeros(nume)

#        xx, yy, sig, Nex, Mex, Vex = stress_beam(U, z, n, mx, my)
#        TESTE.plot(self, U, z, n, sig, mx, my, sig_eq_max)

        return U, z, mx, my, sig_eq_max




