import numpy as np
from PySide6.QtWidgets import QGraphicsOpacityEffect
from PySide6.QtCore import (QPropertyAnimation)

from sampleDatas import SampleData
from saveDatas import SaveDatas

from calculationsCodes.Stress_beam import stress_beam
from calculationsCodes.Displacement_beam import Displacement_beam

import matplotlib.pyplot as plt

class GetGraph():
    def __init__(self):
        super(GetGraph, self).__init__()

    def startFunction(self):
        if self.ui.sampleDataRadioButton.isChecked():
            self.ui.changeData.hide()
            self.ui.initialPage.show()
            self.ui.stackedWidget.setCurrentWidget(self.ui.graphPage)
            self.nume, self.numnp, self.neq, self.P, self.no_P, self.dir_P, self.ndof, self.nodes, self.ns, self.ee, self.b, self.h, self.area, self.Izz, self.coord, self.no,  self.id = SampleData.automaticDatas(self)
            GetGraph.getElement(self, "start")
        else:
            self.ui.changeData.show()
            self.ui.initialPage.hide()
            self.ui.stackedWidget.setCurrentWidget(self.ui.inicialPage)

    def getDataInfo(self):
        self.nume, self.numnp, self.neq, self.P, self.no_P, self.dir_P, self.ndof, self.nodes, self.ns, self.ee, self.b, self.h, self.area, self.Izz, self.coord, self.no,  self.id = SaveDatas.returnInfo(self)  
        GetGraph.getElement(self, "start")

    def getElement(self, type):
        text = self.ui.mainBox.currentText()
        parts = text.split()

        if parts[1].isdigit():
            if type == "start":
                GetGraph.doCalculations(self, int(parts[1])-1)
            else:
                GetGraph.exe(self, int(parts[1])-1)
        else:
            if type == "start":
                GetGraph.doCalculations(self, 0)
            else:
                GetGraph.exe(self, 0)


    def doCalculations(self, n):
        from calculationsCodes.main_beam import MainBeam
        self.U, self.z, self.mx, self.my, self.sig_eq_max = MainBeam.grafico(self, self.nume, self.neq, self.numnp, self.ee, self.area, self.Izz, self.h, self.coord, self.id, self.no, self.P, self.no_P, self.dir_P)
        GetGraph.getSigMax(self)
        GetGraph.exe(self, n)


    def getSigMax(self):
        for n in range (0, self.nume):
            self.xx, self.yy, self.sig, self.Nex, self.Mex, self.Vex = stress_beam(self.U, self.z, n, self.mx, self.my)

            self.SigMax = np.max(self.sig)
            self.SigMax = round(self.SigMax, 2)
            self.sig_eq_max[n] = self.SigMax

    def exe(self, n):
        self.xx, self.yy, self.sig, self.Nex, self.Mex, self.Vex = stress_beam(self.U, self.z, n, self.mx, self.my)
        GetGraph.setData(self)
        GetGraph.plotGraph(self)

    def plotGraph(self):
        if self.ui.mainBox.currentText() != "Full structure":
            self.ui.domainBox.setEnabled(True)
            if self.ui.domainBox.currentText() == "Normal Stress":
                self.ax.clear()
                self.fig.clf()
                self.ax = plt.axes(projection='rectilinear')
                self.ax.plot(self.xx, self.Nex)
                self.ax.set_xlabel('X')
                self.ax.set_ylabel('N(x) - Esforço normal do elemento')
                self.canvas.draw()

            elif self.ui.domainBox.currentText() == "Shear Stress":
                self.ax.clear()
                self.fig.clf()
                self.ax = self.fig.add_subplot(1, 1, 1)
                plt.plot(self.xx, self.Vex)
                plt.xlabel('X')
                plt.ylabel('V(x) - Esforço cortante do elemento')
                self.canvas.draw()

            elif self.ui.domainBox.currentText() == "Moment":
                self.ax.clear()
                self.fig.clf()
                self.ax = self.fig.add_subplot(1, 1, 1)
                plt.plot(self.xx, self.Mex)
                plt.xlabel('X')
                plt.ylabel('M(x) - Momento fletor do elemento')
                self.canvas.draw()

            elif self.ui.domainBox.currentText() == "Von Mises":
                self.ax.clear()
                self.fig.clf()
                self.ax.axis('off')
                self.ax = plt.axes(projection='3d')
                X, Y = np.meshgrid(self.xx, self.yy)
                self.ax.plot_surface(X, Y, self.sig, cmap='jet', vmin=np.nanmin(self.sig), vmax=np.nanmax(self.sig))
                self.ax.view_init(elev=30, azim=-135)  # Ajuste os ângulos elevação (elev) e azimutal (azim) como desejado
                self.ax.set_xlabel('X')
                self.ax.set_ylabel('Y')
                self.ax.set_zlabel('SIG')
                self.canvas.draw()
        else:
            self.ui.domainBox.setEnabled(False)
            self.ui.label_21.setText("-")
            z1, dispNorm, xu, yv, xx, yy = Displacement_beam(self.U, self.z, self.mx)
            self.ax.clear()
            self.fig.clf()
            self.ax = plt.axes(projection='rectilinear')
#            self.ax = self.fig.add_subplot(1, 1, 1)

            for i in range(self.nume):
                self.ax.plot(xu[:, i], yv[:, i], '-')
                self.ax.plot(xx[:, i], yy[:, i], '--')
            self.canvas.draw()

        GetGraph.Resize(self)


    def Resize(self):
        size = self.ui.frame_33.size()
        self.canvas.setGeometry(0, 0, size.width(), size.height())

        self.ax.figure.tight_layout()
        self.canvas.draw()

    def setData(self):
#       Determinação do valor máximo da tensão equivalente de von Mises no n-ésimo elemento
        self.SigMax = np.max(self.sig)
        self.SigMax = self.SigMax / 1000000
        self.SigMax = round(self.SigMax, 2)
        self.ui.label_21.setText(str(f'{self.SigMax} x 10^6'))

#        Determinação da tensão equivalente máxima de von Mises em toda a estrutura
        self.SigMaxMax = np.max(self.sig_eq_max)
        self.SigMaxMax = self.SigMaxMax / 1000000
        self.SigMaxMax = round(self.SigMaxMax, 2)
        self.ui.label_20.setText(str(f'{self.SigMaxMax} x 10^6'))

        # Cálculo das magnitudes máximas de deslocamento em cada elemento e na estrutura
        self.z1, self.dispNorm, self.xu, self.yv, x, y = Displacement_beam(self.U, self.z, self.mx)
        self.dispNorm = round(self.dispNorm, 8)
        self.ui.label_19.setText(str(self.dispNorm))


