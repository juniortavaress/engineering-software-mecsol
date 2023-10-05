import numpy as np

def Fem_data_beam(z):
    # Número total de elementos da estrutura
    nume = 17

    # Número total de nós da estrutura
    numnp = 10

    # Número total de graus de liberdade do problema
    neq = 27

    # Número de graus de liberdade por nó
    ndof = 3

    # Número de nós do elemento
    nodes = 2

    # Número de graus de liberdade do elemento
    ns = nodes * ndof

    # Propriedades do material
    ee = 210e9
    b = 0.02
    h = 0.0729
    area = b * h
    Izz = (b * h ** 3) / 12.0

    #Definição das coordenadas nodais
    #coord[i-1][x]       coord[i-1][y]
    # i = elemento
    # x = 0
    # y = 1

    coord = np.zeros((numnp, 2), dtype=int)
    coord[0][0]=0;      coord[0][1] = 0
    coord[1][0]=2;      coord[1][1] = 0
    coord[2][0]=4;      coord[2][1] = 0
    coord[3][0]=6;      coord[3][1] = 0
    coord[4][0]=8;      coord[4][1] = 0
    coord[5][0]=10;     coord[5][1] = 0
    coord[6][0]=2;      coord[6][1] = 3
    coord[7][0]=4;      coord[7][1] = 4
    coord[8][0]=6;      coord[8][1] = 4
    coord[9][0]=8;      coord[9][1] = 3

    #print("coord", coord)
    #Definição dos graus de liberdade ativos associados a cada no da estrutura
    #id[i-1][u]       id[i-1][v]        id[i-1][teta]
    # i = número do elemento
    # u = 0
    # v = 1
    # teta = 2

    id = np.zeros((numnp, 3), dtype=int)
    id[0][0]=1;      id[0][1] = 0;      id[0][2] = 2
    id[1][0]=3;      id[1][1] = 4;      id[1][2] = 5
    id[2][0]=6;      id[2][1] = 7;      id[2][2] = 8
    id[3][0]=9;      id[3][1] = 10;     id[3][2] = 11
    id[4][0]=12;     id[4][1] = 13;     id[4][2] = 14
    id[5][0]=0;      id[5][1] = 0;      id[5][2] = 15
    id[6][0]=16;     id[6][1] = 17;     id[6][2] = 18
    id[7][0]=19;     id[7][1] = 20;     id[7][2] = 21
    id[8][0]=22;     id[8][1] = 23;     id[8][2] = 24
    id[9][0]=25;     id[9][1] = 26;     id[9][2] = 27

    #print("id", id)
    # Definição da incidência dos nós dos elementos
    #coord[i-1][i1]       coord[i-1][i2]
    # i = número do elemento
    # i1 = 0
    # i2 = 1
    
    no = np.zeros((nume, 2), dtype=int)
    no[0][0]=1;          no[0][1] = 2
    no[1][0]=2;          no[1][1] = 3
    no[2][0]=3;          no[2][1] = 4
    no[3][0]=4;          no[3][1] = 5
    no[4][0]=5;          no[4][1] = 6
    no[5][0]=6;          no[5][1] = 10
    no[6][0]=9;          no[6][1] = 10
    no[7][0]=8;          no[7][1] = 9
    no[8][0]=7;          no[8][1] = 8
    no[9][0]=1;          no[9][1] = 7
    no[10][0]=2;         no[10][1] =7
    no[11][0]=3;         no[11][1] = 7
    no[12][0]=3;         no[12][1] = 8
    no[13][0]=3;         no[13][1] = 9
    no[14][0]=4;         no[14][1] = 9
    no[15][0]=5;         no[15][1] = 9
    no[16][0]=5;         no[16][1] = 10
    #print("no", no)
    return nume, neq, numnp, ee, area, Izz, h, coord.T, id.T, no.T
