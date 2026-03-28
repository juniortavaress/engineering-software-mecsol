import numpy as np
from PySide6.QtCore import QPropertyAnimation
from PySide6.QtWidgets import QGraphicsOpacityEffect


class SaveDatas:
    @staticmethod
    def dadosGerais(window):
        """Compute section properties shared by every beam element."""
        window.ndof = 3
        window.nodes = 2
        window.ns = window.nodes * window.ndof
        window.ee = 210e9
        window.b = 0.02
        window.area = window.b * window.h
        window.Izz = (window.b * window.h**3) / 12

    @staticmethod
    def saveData(window):
        """Read the initial form fields and prepare the next input step."""
        try:
            window.nume = int(window.ui.nume.text())
            window.numnp = int(window.ui.numnp.text())
            window.neq = int(window.ui.neq.text())
            window.P = int(window.ui.P.text())
            window.no_P = int(window.ui.no_P.text())
            window.h = SaveDatas._parse_float(window.ui.h.text())
        except ValueError:
            return

        window.dir_P = SaveDatas._parse_direction(window.ui.dir_P.text())
        SaveDatas._populate_element_selector(window)

        if window.dir_P in {1, 2, 3}:
            SaveDatas.layout(window, "nos")
            SaveDatas.dadosGerais(window)

    @staticmethod
    def saveCoordnodais(window):
        """Read nodal coordinates and advance when the full grid is valid."""
        coordinates = SaveDatas._read_grid(window, "N", window.numnp, 2)
        if coordinates is not None:
            window.coord = coordinates.T
            SaveDatas.layout(window, "elementos")

    @staticmethod
    def saveCoordelement(window):
        """Read the element connectivity matrix and advance when valid."""
        connectivity = SaveDatas._read_grid(window, "E", window.nume, 2)
        if connectivity is not None:
            window.no = connectivity.T
            SaveDatas.layout(window, "graus")

    @staticmethod
    def saveGrausliberdade(window):
        """Read the active degree numbering matrix and open the graph page."""
        dof_map = SaveDatas._read_grid(window, "G", window.numnp, 3, transposed_pattern=True)
        if dof_map is not None:
            window.id = dof_map.T
            window.ui.stackedWidget.setCurrentWidget(window.ui.graphPage)

    @staticmethod
    def returnInfo(window):
        return (
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
        )

    @staticmethod
    def layout(window, page):
        if page == "nos":
            if window.numnp < 11:
                window.ui.frame_97.hide()
                window.ui.frame_14.setMaximumSize(450, 500)

            SaveDatas._show_rows(window, "NO", 20)
            SaveDatas._hide_rows(window, "NO", 20, window.numnp)
            SaveDatas.nextPage(window, window.ui.Nos)

        elif page == "elementos":
            if window.nume < 21:
                window.ui.frame_19.hide()
                window.ui.frame_17.setMaximumSize(450, 800)

            SaveDatas._show_rows(window, "EL", 40)
            SaveDatas._hide_rows(window, "EL", 40, window.nume)
            SaveDatas.nextPage(window, window.ui.Elementos)

        elif page == "graus":
            if window.numnp < 11:
                window.ui.frame_127.hide()
                window.ui.frame_47.setMaximumSize(500, 500)

            SaveDatas._show_rows(window, "GR", 20)
            SaveDatas._hide_rows(window, "GR", 20, window.numnp)
            SaveDatas.nextPage(window, window.ui.Liberdade)

    @staticmethod
    def nextPage(window, page):
        window.ui.stackedWidget.setCurrentWidget(page)
        fade_in = QGraphicsOpacityEffect(page)
        window.animation = QPropertyAnimation(fade_in, b"opacity")
        page.setGraphicsEffect(fade_in)
        window.animation.setDuration(500)
        window.animation.setStartValue(0)
        window.animation.setEndValue(1)
        window.animation.start()

    @staticmethod
    def restart(window):
        SaveDatas._show_rows(window, "NO", 20)
        SaveDatas._show_rows(window, "EL", 40)
        SaveDatas._show_rows(window, "GR", 20)
        window.ui.mainBox.clear()

        if window.ui.saveDataRadioButton.isChecked() and not window.ui.sampleDataRadioButton.isChecked():
            window.ui.stackedWidget.setCurrentWidget(window.ui.inicialPage)
            return

        if window.ui.sampleDataRadioButton.isChecked():
            window.ui.stackedWidget.setCurrentWidget(window.ui.startPage)
            window.ui.sampleDataRadioButton.setChecked(False)
            window.ui.saveDataRadioButton.setChecked(False)
            return

        SaveDatas._clear_grid(window, "N", getattr(window, "numnp", 0), 2)
        SaveDatas._clear_grid(window, "E", getattr(window, "nume", 0), 2)
        SaveDatas._clear_grid(window, "G", getattr(window, "numnp", 0), 3, transposed_pattern=True)
        window.ui.stackedWidget.setCurrentWidget(window.ui.inicialPage)

    @staticmethod
    def _parse_float(value):
        try:
            return float(value)
        except ValueError:
            return float(value.replace(",", "."))

    @staticmethod
    def _parse_direction(value):
        return {"x": 1, "y": 2, "z": 3}.get(value.strip().lower())

    @staticmethod
    def _populate_element_selector(window):
        window.ui.mainBox.clear()
        window.ui.mainBox.addItem("Full structure")
        window.ui.mainBox.addItems([f"Element {index}" for index in range(1, window.nume + 1)])

    @staticmethod
    def _read_grid(window, prefix, row_count, column_count, transposed_pattern=False):
        rows = []
        for row_index in range(1, row_count + 1):
            row = []
            for column_index in range(1, column_count + 1):
                field_name = (
                    f"{prefix}{column_index}{row_index}"
                    if transposed_pattern
                    else f"{prefix}{row_index}{column_index}"
                )
                value = getattr(window.ui, field_name).text().strip()
                if not value:
                    return None
                try:
                    row.append(int(value))
                except ValueError:
                    return None
            rows.append(row)
        return np.array(rows, dtype=int)

    @staticmethod
    def _hide_rows(window, prefix, max_rows, used_rows):
        for row_number in range(used_rows + 1, max_rows + 1):
            getattr(window.ui, f"{prefix}{row_number}").hide()

    @staticmethod
    def _show_rows(window, prefix, max_rows):
        for row_number in range(1, max_rows + 1):
            getattr(window.ui, f"{prefix}{row_number}").show()

    @staticmethod
    def _clear_grid(window, prefix, row_count, column_count, transposed_pattern=False):
        for row_index in range(1, row_count + 1):
            for column_index in range(1, column_count + 1):
                field_name = (
                    f"{prefix}{column_index}{row_index}"
                    if transposed_pattern
                    else f"{prefix}{row_index}{column_index}"
                )
                getattr(window.ui, field_name).setText("")
