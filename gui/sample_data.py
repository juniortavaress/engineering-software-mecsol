import numpy as np


class SampleData:
    @staticmethod
    def automaticDatas(window):
        """Load the fixed sample dataset used by the quick-start GUI option."""
        window.nume = 17
        window.numnp = 10
        window.neq = 27
        window.P = -780000
        window.no_P = 5
        window.dir_P = 2

        window.ndof = 3
        window.nodes = 2
        window.ns = window.nodes * window.ndof
        window.ee = 210e9
        window.b = 0.02
        window.h = 0.0729
        window.area = window.b * window.h
        window.Izz = (window.b * window.h**3) / 12

        window.coord = np.array(
            [[0, 0], [2, 0], [4, 0], [6, 0], [8, 0], [10, 0], [2, 3], [4, 4], [6, 4], [8, 3]],
            dtype=float,
        ).T

        window.no = np.array(
            [
                [1, 2],
                [2, 3],
                [3, 4],
                [4, 5],
                [5, 6],
                [6, 10],
                [9, 10],
                [8, 9],
                [7, 8],
                [1, 7],
                [2, 7],
                [3, 7],
                [3, 8],
                [3, 9],
                [4, 9],
                [5, 9],
                [5, 10],
            ],
            dtype=int,
        ).T

        window.id = np.array(
            [
                [1, 0, 2],
                [3, 4, 5],
                [6, 7, 8],
                [9, 10, 11],
                [12, 13, 14],
                [0, 0, 15],
                [16, 17, 18],
                [19, 20, 21],
                [22, 23, 24],
                [25, 26, 27],
            ],
            dtype=int,
        ).T

        SampleData._populate_element_selector(window)

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
    def _populate_element_selector(window):
        window.ui.mainBox.clear()
        window.ui.mainBox.addItem("Full structure")
        window.ui.mainBox.addItems([f"Element {index}" for index in range(1, window.nume + 1)])
