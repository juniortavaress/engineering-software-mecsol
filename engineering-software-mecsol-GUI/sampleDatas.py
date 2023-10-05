import numpy as np
from PySide6.QtWidgets import QGraphicsOpacityEffect
from PySide6.QtCore import (QPropertyAnimation)

class SampleData():
    def __init__(self):
        super(SampleData, self).__init__()


    def automaticDatas(self):
#        global numnp, nume, neq, P, no_P, dir_P, ndof, nodes, ns, ee, b, h, area, Izz, z, ro, gx, gy, kk, F, coord, no, id
        self.nume = 17
        self.numnp = 10
        self.neq = 27
        self.P = -780000
        self.no_P = 5
        self.dir_P = 2

        self.ndof = 3
        self.nodes = 2
        self.ns = self.nodes * self.ndof
        self.ee = 210e9
        self.b = 0.02
        self.h = 0.0729
        self.area = self.b * self.h
        self.Izz = (self.b * self.h ** 3)/12

        self.coord = [[0, 0], [2, 0], [4, 0], [6, 0], [8, 0], [10, 0], [2, 3], [4, 4], [6, 4], [8, 3]]
        self.coord = np.array(self.coord, dtype=object)
        self.coord = self.coord.T

        self.no = [[1, 2], [2, 3], [3, 4], [4, 5],    [5, 6], [6, 10], [9, 10], [8, 9], [7, 8], [1, 7], [2, 7], [3, 7], [3, 8], [3, 9], [4, 9], [5, 9], [5, 10]]
        self.no = np.array(self.no, dtype=object)
        self.no = self.no.T

        self.id = [[1, 0, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14], [0, 0, 15], [16, 17, 18], [19, 20, 21], [22, 23, 24], [25, 26, 27]]
        self.id = np.array(self.id, dtype=object)
        self.id = self.id.T

        for i in range (1, 18):
            self.ui.mainBox.addItems([f'Element {i}'])
#        self.ui.mainBox.setCurrentIndex(1)

        return self.nume, self.numnp, self.neq, self.P, self.no_P, self.dir_P, self.ndof, self.nodes, self.ns, self.ee, self.b, self.h, self.area, self.Izz, self.coord, self.no,  self.id





