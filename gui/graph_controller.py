import matplotlib.pyplot as plt
import numpy as np

from beam_analysis.displacement_beam import displacement_beam
from beam_analysis.stress_beam import stress_beam
from gui.sample_data import SampleData
from gui.data_entry import SaveDatas


class GetGraph:
    @staticmethod
    def startFunction(window):
        if window.ui.sampleDataRadioButton.isChecked():
            window.ui.changeData.hide()
            window.ui.initialPage.show()
            window.ui.stackedWidget.setCurrentWidget(window.ui.graphPage)
            (
                window.nume,
                window.numnp,
                window.neq,
                window.P,
                window.no_P,
                window.dir_P,
                window.ndof,
                window.nodes,
                window.ns,
                window.ee,
                window.b,
                window.h,
                window.area,
                window.Izz,
                window.coord,
                window.no,
                window.id,
            ) = SampleData.automaticDatas(window)
            GetGraph.getElement(window, "start")
            return

        window.ui.changeData.show()
        window.ui.initialPage.hide()
        window.ui.stackedWidget.setCurrentWidget(window.ui.inicialPage)

    @staticmethod
    def getDataInfo(window):
        (
            window.nume,
            window.numnp,
            window.neq,
            window.P,
            window.no_P,
            window.dir_P,
            window.ndof,
            window.nodes,
            window.ns,
            window.ee,
            window.b,
            window.h,
            window.area,
            window.Izz,
            window.coord,
            window.no,
            window.id,
        ) = SaveDatas.returnInfo(window)
        GetGraph.getElement(window, "start")

    @staticmethod
    def getElement(window, event_type):
        parts = window.ui.mainBox.currentText().split()
        selected_index = int(parts[1]) - 1 if len(parts) > 1 and parts[1].isdigit() else 0

        if event_type != "start" and not hasattr(window, "U"):
            return

        if event_type == "start":
            GetGraph.doCalculations(window, selected_index)
        else:
            GetGraph.exe(window, selected_index)

    @staticmethod
    def doCalculations(window, element_index):
        from beam_analysis.main_beam import MainBeam

        (
            window.U,
            window.z,
            window.mx,
            window.my,
            window.sig_eq_max,
        ) = MainBeam.solve_structure(
            window.nume,
            window.neq,
            window.ee,
            window.area,
            window.Izz,
            window.coord,
            window.id,
            window.no,
            window.P,
            window.no_P,
            window.dir_P,
        )
        GetGraph.getSigMax(window)
        GetGraph.exe(window, element_index)

    @staticmethod
    def getSigMax(window):
        for element_index in range(window.nume):
            (
                window.xx,
                window.yy,
                window.sig,
                window.Nex,
                window.Mex,
                window.Vex,
            ) = stress_beam(window.U, element_index, window.mx, window.my)

            window.SigMax = round(np.max(window.sig), 2)
            window.sig_eq_max[element_index] = window.SigMax

    @staticmethod
    def exe(window, element_index):
        (
            window.xx,
            window.yy,
            window.sig,
            window.Nex,
            window.Mex,
            window.Vex,
        ) = stress_beam(window.U, element_index, window.mx, window.my)
        GetGraph.setData(window)
        GetGraph.plotGraph(window)

    @staticmethod
    def plotGraph(window):
        if window.ui.mainBox.currentText() != "Full structure":
            window.ui.domainBox.setEnabled(True)
            domain = window.ui.domainBox.currentText()

            if domain == "Normal Stress":
                window.ax.clear()
                window.fig.clf()
                window.ax = plt.axes(projection="rectilinear")
                window.ax.plot(window.xx, window.Nex)
                window.ax.set_xlabel("X")
                window.ax.set_ylabel("N(x) - EsforÃ§o normal do elemento")
                window.canvas.draw()

            elif domain == "Shear Stress":
                window.ax.clear()
                window.fig.clf()
                window.ax = window.fig.add_subplot(1, 1, 1)
                plt.plot(window.xx, window.Vex)
                plt.xlabel("X")
                plt.ylabel("V(x) - EsforÃ§o cortante do elemento")
                window.canvas.draw()

            elif domain == "Moment":
                window.ax.clear()
                window.fig.clf()
                window.ax = window.fig.add_subplot(1, 1, 1)
                plt.plot(window.xx, window.Mex)
                plt.xlabel("X")
                plt.ylabel("M(x) - Momento fletor do elemento")
                window.canvas.draw()

            elif domain == "Von Mises":
                window.ax.clear()
                window.fig.clf()
                window.ax.axis("off")
                window.ax = plt.axes(projection="3d")
                x_grid, y_grid = np.meshgrid(window.xx, window.yy)
                window.ax.plot_surface(
                    x_grid,
                    y_grid,
                    window.sig,
                    cmap="jet",
                    vmin=np.nanmin(window.sig),
                    vmax=np.nanmax(window.sig),
                )
                window.ax.view_init(elev=30, azim=-135)
                window.ax.set_xlabel("X")
                window.ax.set_ylabel("Y")
                window.ax.set_zlabel("SIG")
                window.canvas.draw()
        else:
            window.ui.domainBox.setEnabled(False)
            window.ui.label_21.setText("-")
            disp_norm, x_deformed, y_deformed, x_initial, y_initial = displacement_beam(
                window.U, window.mx
            )
            window.ax.clear()
            window.fig.clf()
            window.ax = plt.axes(projection="rectilinear")

            for element_index in range(window.nume):
                window.ax.plot(x_deformed[:, element_index], y_deformed[:, element_index], "-")
                window.ax.plot(x_initial[:, element_index], y_initial[:, element_index], "--")
            window.canvas.draw()

        GetGraph.Resize(window)

    @staticmethod
    def Resize(window):
        size = window.ui.frame_33.size()
        window.canvas.setGeometry(0, 0, size.width(), size.height())
        window.ax.figure.tight_layout()
        window.canvas.draw()

    @staticmethod
    def setData(window):
        window.SigMax = round(np.max(window.sig) / 1_000_000, 2)
        window.ui.label_21.setText(f"{window.SigMax} x 10^6")

        window.SigMaxMax = round(np.max(window.sig_eq_max) / 1_000_000, 2)
        window.ui.label_20.setText(f"{window.SigMaxMax} x 10^6")

        window.dispNorm, window.xu, window.yv, x_initial, y_initial = displacement_beam(
            window.U, window.mx
        )
        window.dispNorm = round(window.dispNorm, 8)
        window.ui.label_19.setText(str(window.dispNorm))

