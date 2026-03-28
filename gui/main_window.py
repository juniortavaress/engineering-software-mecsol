import sys

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow

from gui.data_entry import SaveDatas
from gui.graph_controller import GetGraph
from ui.ui_form import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self._setup_canvas()
        self.resizeEvent = self._resize_graph
        self.ui.stackedWidget.setCurrentWidget(self.ui.startPage)
        self.ui.exportFig.setEnabled(True)

        self.ui.startButton.clicked.connect(lambda: GetGraph.startFunction(self))
        self.ui.nextButtonInitial.clicked.connect(lambda: SaveDatas.saveData(self))
        self.ui.nextButtonNo.clicked.connect(lambda: SaveDatas.saveCoordnodais(self))
        self.ui.nextButtonIncidencias.clicked.connect(lambda: SaveDatas.saveCoordelement(self))
        self.ui.nextButtonLiberdade.clicked.connect(lambda: SaveDatas.saveGrausliberdade(self))
        self.ui.nextButtonLiberdade.clicked.connect(lambda: GetGraph.getDataInfo(self))
        self.ui.domainBox.currentIndexChanged.connect(lambda: GetGraph.plotGraph(self))
        self.ui.mainBox.currentIndexChanged.connect(lambda: GetGraph.getElement(self, "change"))
        self.ui.changeData.clicked.connect(lambda: SaveDatas.restart(self))
        self.ui.initialPage.clicked.connect(lambda: SaveDatas.restart(self))
        self.ui.exportFig.clicked.connect(self.export_figure)

    def _setup_canvas(self):
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlabel("X")
        self.ax.set_ylabel("Y")
        self.ax.relim()
        self.ax.autoscale_view()
        self.canvas = FigureCanvas(self.fig)
        size = self.ui.frame_33.size()
        self.canvas.setGeometry(0, 0, size.width(), size.height())
        self.canvas.setGeometry(self.ui.frame_33.contentsRect())
        self.canvas.setParent(self.ui.frame_33)

    def _resize_graph(self, event):
        size = self.ui.frame_33.size()
        self.canvas.setGeometry(0, 0, size.width(), size.height())
        self.ax.set_aspect("auto")
        self.ax.figure.tight_layout()
        self.canvas.draw()
        super().resizeEvent(event)

    def export_figure(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Salvar Gráfico",
            "",
            "Imagens PNG (*.png);;Todos os arquivos (*)",
            options=options,
        )

        if file_path:
            self.fig.savefig(file_path)


def run():
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
