import numpy as np
from PySide6.QtWidgets import QGraphicsOpacityEffect
from PySide6.QtCore import (QPropertyAnimation)



class SaveDatas():
    def __init__(self):
        super(SaveDatas, self).__init__()

    def dadosGerais(self):
        #global ndof, nodes, ns, ee, b, h, area, Izz, z, ro, gx, gy, kk, F
        self.ndof = 3
        self.nodes = 2
        self.ns = self.nodes * self.ndof
        self.ee = 210e9
        self.b = 0.02
#        self.h = 0.0729
        self.area = self.b * self.h
        self.Izz = (self.b * self.h ** 3)/12

    def saveData(self):
        #global numnp, nume, neq, P, no_P, dir_P
        self.nume = int(self.ui.nume.text())                                     #Número de Elementos
        self.numnp = int(self.ui.numnp.text())                                   #Número de Nós
        self.neq = int(self.ui.neq.text())                                       #Número de graus de liberdade total
        self.P = int(self.ui.P.text())                                           #Carga aplicada
        self.no_P = int(self.ui.no_P.text())                                     #Nó da carga
        self.dir_P = self.ui.dir_P.text()                                        #Direção da aplicação

        try:
            self.h = float(self.ui.h.text())                                     #Espessura dos elementos
        except:
            self.h = float(self.ui.h.text().replace(',', '.'))

        for i in range (1, self.nume+1):
            self.ui.mainBox.addItems([f'Element {i}'])
        #self.ui.mainBox.setCurrentIndex(2)

        if self.nume and self.numnp and self.neq and self.P and self.no_P and self.dir_P != "":
            if self.dir_P == "x" or self.dir_P == "X":
               self.dir_P = 1

            elif self.dir_P == "y" or self.dir_P == "Y":
              self.dir_P = 2

            elif self.dir_P == "z" or self.dir_P == "Z":
              self.dir_P = 3


        if self.dir_P == 1 or self.dir_P == 2 or self.dir_P ==3:
            SaveDatas.layout(self, "nos")
            SaveDatas.dadosGerais(self)
        else:
            pass


    def saveCoordnodais(self):                                              #Função para criar lista com valores das coordenadas nodais
        #global coord
        elementos = []
        for i in range(1, self.numnp+1): #numnp+1
            elemento = []
            for j in range(1, 3):
                valor = getattr(self.ui, f'N{i}{j}').text()
                if valor:
                    try:
                        valor = int(valor)
                    except:
                        pass
#                        print("Valores Incorretos")
                else:
                    pass
#                    print("Valores Incompletos")
                elemento.append(valor)
            elementos.append(elemento)
        coord = np.array(elementos, dtype=object)

        for linha in coord:
            for valor in linha:
                if isinstance(valor, int):
                    y=0
                else:
                    y=1
        if y !=1:
            SaveDatas.layout(self, "elementos")
        self.coord = coord.T


    def saveCoordelement(self):                                             #Função para criar lista com valores dos nós por elementos
        #global no
        nos = []
        for i in range(1, self.nume+1): #nume+1
            noi = []
            for j in range(1, 3):
                valor = getattr(self.ui, f'E{i}{j}').text()
                if valor:
                    try:
                        valor = int(valor)

                    except:
                        pass
#                    print("Valores Incorretos")
                else:
                    print("Valores Incompletos")
                noi.append(valor)
            nos.append(noi)
        no = np.array(nos, dtype=object)

        for linha in no:
            for valor in linha:
                if isinstance(valor, int):
                    y=0
                else:
                    y=1
        if y !=1:
            SaveDatas.layout(self, "graus")
        self.no = no.T


    def saveGrausliberdade(self):                                             #Função para criar lista com valores dos graus de liberdade
        graus = []
        for i in range(1, self.numnp+1): #numnp+1
            grau = []
            for j in range(1, 4):
                valor = getattr(self.ui, f'G{j}{i}').text()
                if valor:
                    try:
                        valor = int(valor)
                    except:
                        pass
#                        print("Valores Incorretos")
                else:
                    pass
#                    print("Valores Incompletos")
                grau.append(valor)
            graus.append(grau)
        id = np.array(graus, dtype=object)

        for linha in id:
            for valor in linha:
                if isinstance(valor, int):
                    y=0
                else:
                    y=1
        if y !=1:
#            print("aqui")
            self.ui.stackedWidget.setCurrentWidget(self.ui.graphPage) 
        self.id = id.T
        
    def returnInfo(self):
        return self.nume, self.numnp, self.neq, self.P, self.no_P, self.dir_P, self.ndof, self.nodes, self.ns, self.ee, self.b, self.h, self.area, self.Izz, self.coord, self.no,  self.id

    def layout(self, page):
        if page == "nos":
            if self.numnp < 11:
                self.ui.frame_97.hide()
                self.ui.frame_14.setMaximumSize(450, 500)

            hide = []
            for x in range(20 - self.numnp, 0, -1):
                y = 21 - x
                hide.append(y)
                node = getattr(self.ui, f'NO{y}')
                node.hide()

            SaveDatas.nextPage(self, self.ui.Nos)


        elif page == "elementos":
            if self.nume < 21:
                self.ui.frame_19.hide()
                self.ui.frame_17.setMaximumSize(450, 800)

            hide = []
            for x in range(40 - self.nume, 0, -1):
                y = 41 - x
                hide.append(y)
                node = getattr(self.ui, f'EL{y}')
                node.hide()

            SaveDatas.nextPage(self, self.ui.Elementos)

        elif page == "graus":
            if self.numnp < 11:
                self.ui.frame_127.hide()
                self.ui.frame_47.setMaximumSize(500, 500)

            hide = []
            for x in range(20 - self.numnp, 0, -1):
                y = 21 - x
                hide.append(y)
                node = getattr(self.ui, f'GR{y}')
                node.hide()

            SaveDatas.nextPage(self, self.ui.Liberdade)

    def nextPage(self, page):
        self.ui.stackedWidget.setCurrentWidget(page)
        fadeIn = QGraphicsOpacityEffect(page)
        self.animation = QPropertyAnimation(fadeIn, b"opacity")
        page.setGraphicsEffect(fadeIn)
        self.animation.setDuration(500)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()

    def restart(self):
        if self.ui.saveDataRadioButton.isChecked() and not self.ui.sampleDataRadioButton.isChecked():
            self.ui.stackedWidget.setCurrentWidget(self.ui.inicialPage)

        elif self.ui.sampleDataRadioButton.isChecked():
            self.ui.stackedWidget.setCurrentWidget(self.ui.startPage)
            self.ui.sampleDataRadioButton.setChecked(False)
            self.ui.saveDataRadioButton.setChecked(False)

        else: 
            for i in range(1, self.numnp+1): #numnp+1
                for j in range(1, 3):
                    valor = getattr(self.ui, f'N{i}{j}')
                    valor.setText("")
                
            for i in range(1, self.nume+1): #nume+1
                for j in range(1, 3):
                    valor = getattr(self.ui, f'E{i}{j}')
                    valor.setText("")

            for i in range(1, self.numnp+1): #numnp+1
                for j in range(1, 4):
                    valor = getattr(self.ui, f'G{j}{i}')
                    valor.setText("")
            self.ui.stackedWidget.setCurrentWidget(self.ui.inicialPage)
