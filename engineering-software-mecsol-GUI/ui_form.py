# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)
import img_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1527, 823)
        icon = QIcon()
        icon.addFile(u":/icons/img/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Cabecalho = QFrame(self.centralwidget)
        self.Cabecalho.setObjectName(u"Cabecalho")
        self.Cabecalho.setMinimumSize(QSize(0, 60))
        self.Cabecalho.setMaximumSize(QSize(16777215, 60))
        self.Cabecalho.setStyleSheet(u"background-color: rgb(38, 40, 61);")
        self.Cabecalho.setFrameShape(QFrame.StyledPanel)
        self.Cabecalho.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.Cabecalho)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.Cabecalho)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.label)


        self.verticalLayout.addWidget(self.Cabecalho)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(195, 195, 195);")
        self.inicialPage = QWidget()
        self.inicialPage.setObjectName(u"inicialPage")
        self.verticalLayout_6 = QVBoxLayout(self.inicialPage)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.inicialPage)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(195, 195, 195);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(450, 450))
        font = QFont()
        font.setPointSize(21)
        self.frame_4.setFont(font)
        self.frame_4.setStyleSheet(u"QFrame{\n"
"background-color: rgb(148, 147, 150);\n"
"border-radius: 6px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: rgb(217, 217, 217);\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 5px;\n"
"    padding: 0px;\n"
"    font-size: 14px;\n"
"    color: #333;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color: rgb(217, 217, 217);\n"
"    border: 1px solid #66afe9;\n"
"    outline: none;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.frame_5.setFont(font1)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid rgb(38, 40, 61);\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.frame_7)
        self.label_3.setObjectName(u"label_3")
        font3 = QFont()
        font3.setPointSize(11)
        self.label_3.setFont(font3)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.nume = QLineEdit(self.frame_7)
        self.nume.setObjectName(u"nume")
        self.nume.setMinimumSize(QSize(100, 0))
        self.nume.setMaximumSize(QSize(100, 16777215))
        self.nume.setMouseTracking(False)
        self.nume.setStyleSheet(u"")
        self.nume.setAlignment(Qt.AlignCenter)
        self.nume.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_2.addWidget(self.nume)


        self.verticalLayout_5.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.frame_8)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.numnp = QLineEdit(self.frame_8)
        self.numnp.setObjectName(u"numnp")
        self.numnp.setMinimumSize(QSize(100, 0))
        self.numnp.setMaximumSize(QSize(100, 16777215))
        self.numnp.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.numnp)


        self.verticalLayout_5.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.frame_9)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.neq = QLineEdit(self.frame_9)
        self.neq.setObjectName(u"neq")
        self.neq.setMinimumSize(QSize(100, 0))
        self.neq.setMaximumSize(QSize(100, 16777215))
        self.neq.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.neq)


        self.verticalLayout_5.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_6)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.frame_10)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)

        self.horizontalLayout_5.addWidget(self.label_6)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.P = QLineEdit(self.frame_10)
        self.P.setObjectName(u"P")
        self.P.setMinimumSize(QSize(100, 0))
        self.P.setMaximumSize(QSize(100, 16777215))
        self.P.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.P)


        self.verticalLayout_5.addWidget(self.frame_10)

        self.frame_12 = QFrame(self.frame_6)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_8 = QLabel(self.frame_12)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font3)

        self.horizontalLayout_7.addWidget(self.label_8)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)

        self.no_P = QLineEdit(self.frame_12)
        self.no_P.setObjectName(u"no_P")
        self.no_P.setMinimumSize(QSize(100, 0))
        self.no_P.setMaximumSize(QSize(100, 16777215))
        self.no_P.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.no_P)


        self.verticalLayout_5.addWidget(self.frame_12)

        self.frame_72 = QFrame(self.frame_6)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_72)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.label_13 = QLabel(self.frame_72)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font3)

        self.horizontalLayout_55.addWidget(self.label_13)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_55.addItem(self.horizontalSpacer_8)

        self.h = QLineEdit(self.frame_72)
        self.h.setObjectName(u"h")
        self.h.setMinimumSize(QSize(100, 0))
        self.h.setMaximumSize(QSize(100, 16777215))
        self.h.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_55.addWidget(self.h)


        self.verticalLayout_5.addWidget(self.frame_72)

        self.frame_11 = QFrame(self.frame_6)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(self.frame_11)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)

        self.horizontalLayout_6.addWidget(self.label_7)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.dir_P = QLineEdit(self.frame_11)
        self.dir_P.setObjectName(u"dir_P")
        self.dir_P.setMinimumSize(QSize(100, 0))
        self.dir_P.setMaximumSize(QSize(100, 16777215))
        self.dir_P.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.dir_P)


        self.verticalLayout_5.addWidget(self.frame_11)

        self.frame_13 = QFrame(self.frame_6)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 5, -1, -1)
        self.nextButtonInitial = QPushButton(self.frame_13)
        self.nextButtonInitial.setObjectName(u"nextButtonInitial")
        self.nextButtonInitial.setMinimumSize(QSize(0, 30))
        self.nextButtonInitial.setMaximumSize(QSize(150, 16777215))
        font4 = QFont()
        font4.setPointSize(12)
        self.nextButtonInitial.setFont(font4)
        self.nextButtonInitial.setStyleSheet(u"QPushButton {\n"
"	padding-left: 5px;\n"
"	background-color: rgb(38, 40, 61);\n"
"	border:none;\n"
"	border-radius:15px;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 3px solid;\n"
"	background-color:rgb(241, 102, 55);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color:rgb(241, 102, 55);\n"
"}\n"
"")
        self.nextButtonInitial.setAutoRepeatDelay(301)

        self.horizontalLayout_8.addWidget(self.nextButtonInitial)


        self.verticalLayout_5.addWidget(self.frame_13)


        self.verticalLayout_2.addWidget(self.frame_6)


        self.horizontalLayout.addWidget(self.frame_4)


        self.verticalLayout_6.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.inicialPage)
        self.Nos = QWidget()
        self.Nos.setObjectName(u"Nos")
        self.horizontalLayout_16 = QHBoxLayout(self.Nos)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.frame_14 = QFrame(self.Nos)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 500))
        self.frame_14.setMaximumSize(QSize(900, 500))
        self.frame_14.setFont(font)
        self.frame_14.setStyleSheet(u"QFrame{\n"
"background-color: rgb(148, 147, 150);\n"
"border-radius: 6px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: rgb(217, 217, 217);\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 5px;\n"
"    padding: 0px;\n"
"    font-size: 14px;\n"
"    color: #333;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color: rgb(217, 217, 217);\n"
"    border: 1px solid #66afe9;\n"
"    outline: none;\n"
"}")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_14)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(16777215, 40))
        self.frame_15.setFont(font1)
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_15)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_10 = QLabel(self.frame_15)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_10)


        self.verticalLayout_8.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.frame_14)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid rgb(38, 40, 61);\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_16)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_16)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_111 = QHBoxLayout(self.frame)
        self.horizontalLayout_111.setSpacing(30)
        self.horizontalLayout_111.setObjectName(u"horizontalLayout_111")
        self.horizontalLayout_111.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_3)
        self.verticalLayout_24.setSpacing(8)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.frame_100 = QFrame(self.frame_3)
        self.frame_100.setObjectName(u"frame_100")
        self.frame_100.setMinimumSize(QSize(0, 40))
        self.frame_100.setMaximumSize(QSize(16777215, 40))
        self.frame_100.setFrameShape(QFrame.StyledPanel)
        self.frame_100.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_100)
        self.verticalLayout_35.setSpacing(3)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 10)
        self.frame_101 = QFrame(self.frame_100)
        self.frame_101.setObjectName(u"frame_101")
        self.frame_101.setFrameShape(QFrame.StyledPanel)
        self.frame_101.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_100 = QHBoxLayout(self.frame_101)
        self.horizontalLayout_100.setSpacing(50)
        self.horizontalLayout_100.setObjectName(u"horizontalLayout_100")
        self.horizontalLayout_100.setContentsMargins(0, 0, 0, 0)
        self.label_123 = QLabel(self.frame_101)
        self.label_123.setObjectName(u"label_123")
        self.label_123.setMaximumSize(QSize(50, 16777215))
        font5 = QFont()
        font5.setPointSize(13)
        font5.setBold(True)
        self.label_123.setFont(font5)
        self.label_123.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_100.addWidget(self.label_123)

        self.label_124 = QLabel(self.frame_101)
        self.label_124.setObjectName(u"label_124")
        self.label_124.setMaximumSize(QSize(50, 16777215))
        self.label_124.setFont(font5)
        self.label_124.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_100.addWidget(self.label_124)

        self.label_125 = QLabel(self.frame_101)
        self.label_125.setObjectName(u"label_125")
        self.label_125.setMaximumSize(QSize(50, 16777215))
        self.label_125.setFont(font5)
        self.label_125.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_100.addWidget(self.label_125)


        self.verticalLayout_35.addWidget(self.frame_101)

        self.line_7 = QFrame(self.frame_100)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setMinimumSize(QSize(0, 2))
        self.line_7.setMaximumSize(QSize(16777215, 2))
        self.line_7.setStyleSheet(u"border: 1px solid rgb(0, 0, 0);")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_35.addWidget(self.line_7)


        self.verticalLayout_24.addWidget(self.frame_100)

        self.NO1 = QFrame(self.frame_3)
        self.NO1.setObjectName(u"NO1")
        self.NO1.setFrameShape(QFrame.StyledPanel)
        self.NO1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_83 = QHBoxLayout(self.NO1)
        self.horizontalLayout_83.setSpacing(0)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.horizontalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.label_102 = QLabel(self.NO1)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setMaximumSize(QSize(110, 16777215))
        font6 = QFont()
        font6.setPointSize(13)
        self.label_102.setFont(font6)
        self.label_102.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_83.addWidget(self.label_102)

        self.horizontalSpacer_166 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_83.addItem(self.horizontalSpacer_166)

        self.N11 = QLineEdit(self.NO1)
        self.N11.setObjectName(u"N11")
        self.N11.setMinimumSize(QSize(50, 0))
        self.N11.setMaximumSize(QSize(50, 16777215))
        self.N11.setMouseTracking(False)
        self.N11.setStyleSheet(u"")
        self.N11.setAlignment(Qt.AlignCenter)
        self.N11.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_83.addWidget(self.N11)

        self.horizontalSpacer_167 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_83.addItem(self.horizontalSpacer_167)

        self.N12 = QLineEdit(self.NO1)
        self.N12.setObjectName(u"N12")
        self.N12.setMinimumSize(QSize(50, 0))
        self.N12.setMaximumSize(QSize(50, 16777215))
        self.N12.setMouseTracking(False)
        self.N12.setStyleSheet(u"")
        self.N12.setAlignment(Qt.AlignCenter)
        self.N12.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_83.addWidget(self.N12)

        self.horizontalSpacer_168 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_83.addItem(self.horizontalSpacer_168)


        self.verticalLayout_24.addWidget(self.NO1)

        self.NO2 = QFrame(self.frame_3)
        self.NO2.setObjectName(u"NO2")
        self.NO2.setFrameShape(QFrame.StyledPanel)
        self.NO2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_82 = QHBoxLayout(self.NO2)
        self.horizontalLayout_82.setSpacing(0)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.horizontalLayout_82.setContentsMargins(0, 0, 0, 0)
        self.label_101 = QLabel(self.NO2)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setMaximumSize(QSize(110, 16777215))
        self.label_101.setFont(font6)
        self.label_101.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_82.addWidget(self.label_101)

        self.horizontalSpacer_163 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_82.addItem(self.horizontalSpacer_163)

        self.N21 = QLineEdit(self.NO2)
        self.N21.setObjectName(u"N21")
        self.N21.setMinimumSize(QSize(50, 0))
        self.N21.setMaximumSize(QSize(50, 16777215))
        self.N21.setMouseTracking(False)
        self.N21.setStyleSheet(u"")
        self.N21.setAlignment(Qt.AlignCenter)
        self.N21.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_82.addWidget(self.N21)

        self.horizontalSpacer_164 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_82.addItem(self.horizontalSpacer_164)

        self.N22 = QLineEdit(self.NO2)
        self.N22.setObjectName(u"N22")
        self.N22.setMinimumSize(QSize(50, 0))
        self.N22.setMaximumSize(QSize(50, 16777215))
        self.N22.setMouseTracking(False)
        self.N22.setStyleSheet(u"")
        self.N22.setAlignment(Qt.AlignCenter)
        self.N22.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_82.addWidget(self.N22)

        self.horizontalSpacer_165 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_82.addItem(self.horizontalSpacer_165)


        self.verticalLayout_24.addWidget(self.NO2)

        self.NO3 = QFrame(self.frame_3)
        self.NO3.setObjectName(u"NO3")
        self.NO3.setFrameShape(QFrame.StyledPanel)
        self.NO3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_84 = QHBoxLayout(self.NO3)
        self.horizontalLayout_84.setSpacing(0)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.horizontalLayout_84.setContentsMargins(0, 0, 0, 0)
        self.label_103 = QLabel(self.NO3)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setMaximumSize(QSize(110, 16777215))
        self.label_103.setFont(font6)
        self.label_103.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_84.addWidget(self.label_103)

        self.horizontalSpacer_169 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_84.addItem(self.horizontalSpacer_169)

        self.N31 = QLineEdit(self.NO3)
        self.N31.setObjectName(u"N31")
        self.N31.setMinimumSize(QSize(50, 0))
        self.N31.setMaximumSize(QSize(50, 16777215))
        self.N31.setMouseTracking(False)
        self.N31.setStyleSheet(u"")
        self.N31.setAlignment(Qt.AlignCenter)
        self.N31.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_84.addWidget(self.N31)

        self.horizontalSpacer_170 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_84.addItem(self.horizontalSpacer_170)

        self.N32 = QLineEdit(self.NO3)
        self.N32.setObjectName(u"N32")
        self.N32.setMinimumSize(QSize(50, 0))
        self.N32.setMaximumSize(QSize(50, 16777215))
        self.N32.setMouseTracking(False)
        self.N32.setStyleSheet(u"")
        self.N32.setAlignment(Qt.AlignCenter)
        self.N32.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_84.addWidget(self.N32)

        self.horizontalSpacer_171 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_84.addItem(self.horizontalSpacer_171)


        self.verticalLayout_24.addWidget(self.NO3)

        self.NO4 = QFrame(self.frame_3)
        self.NO4.setObjectName(u"NO4")
        self.NO4.setFrameShape(QFrame.StyledPanel)
        self.NO4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_80 = QHBoxLayout(self.NO4)
        self.horizontalLayout_80.setSpacing(0)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.horizontalLayout_80.setContentsMargins(0, 0, 0, 0)
        self.label_99 = QLabel(self.NO4)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setMaximumSize(QSize(110, 16777215))
        self.label_99.setFont(font6)
        self.label_99.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_80.addWidget(self.label_99)

        self.a = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_80.addItem(self.a)

        self.N41 = QLineEdit(self.NO4)
        self.N41.setObjectName(u"N41")
        self.N41.setMinimumSize(QSize(50, 0))
        self.N41.setMaximumSize(QSize(50, 16777215))
        self.N41.setMouseTracking(False)
        self.N41.setStyleSheet(u"")
        self.N41.setAlignment(Qt.AlignCenter)
        self.N41.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_80.addWidget(self.N41)

        self.horizontalSpacer_158 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_80.addItem(self.horizontalSpacer_158)

        self.N42 = QLineEdit(self.NO4)
        self.N42.setObjectName(u"N42")
        self.N42.setMinimumSize(QSize(50, 0))
        self.N42.setMaximumSize(QSize(50, 16777215))
        self.N42.setMouseTracking(False)
        self.N42.setStyleSheet(u"")
        self.N42.setAlignment(Qt.AlignCenter)
        self.N42.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_80.addWidget(self.N42)

        self.horizontalSpacer_159 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_80.addItem(self.horizontalSpacer_159)


        self.verticalLayout_24.addWidget(self.NO4)

        self.NO5 = QFrame(self.frame_3)
        self.NO5.setObjectName(u"NO5")
        self.NO5.setFrameShape(QFrame.StyledPanel)
        self.NO5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_78 = QHBoxLayout(self.NO5)
        self.horizontalLayout_78.setSpacing(0)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.horizontalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.label_97 = QLabel(self.NO5)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setMaximumSize(QSize(110, 16777215))
        self.label_97.setFont(font6)
        self.label_97.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_78.addWidget(self.label_97)

        self.horizontalSpacer_151 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_78.addItem(self.horizontalSpacer_151)

        self.N51 = QLineEdit(self.NO5)
        self.N51.setObjectName(u"N51")
        self.N51.setMinimumSize(QSize(50, 0))
        self.N51.setMaximumSize(QSize(50, 16777215))
        self.N51.setMouseTracking(False)
        self.N51.setStyleSheet(u"")
        self.N51.setAlignment(Qt.AlignCenter)
        self.N51.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_78.addWidget(self.N51)

        self.horizontalSpacer_152 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_78.addItem(self.horizontalSpacer_152)

        self.N52 = QLineEdit(self.NO5)
        self.N52.setObjectName(u"N52")
        self.N52.setMinimumSize(QSize(50, 0))
        self.N52.setMaximumSize(QSize(50, 16777215))
        self.N52.setMouseTracking(False)
        self.N52.setStyleSheet(u"")
        self.N52.setAlignment(Qt.AlignCenter)
        self.N52.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_78.addWidget(self.N52)

        self.horizontalSpacer_153 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_78.addItem(self.horizontalSpacer_153)


        self.verticalLayout_24.addWidget(self.NO5)

        self.NO6 = QFrame(self.frame_3)
        self.NO6.setObjectName(u"NO6")
        self.NO6.setFrameShape(QFrame.StyledPanel)
        self.NO6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_87 = QHBoxLayout(self.NO6)
        self.horizontalLayout_87.setSpacing(0)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.horizontalLayout_87.setContentsMargins(0, 0, 0, 0)
        self.label_106 = QLabel(self.NO6)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setMaximumSize(QSize(110, 16777215))
        self.label_106.setFont(font6)
        self.label_106.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_87.addWidget(self.label_106)

        self.horizontalSpacer_178 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_87.addItem(self.horizontalSpacer_178)

        self.N61 = QLineEdit(self.NO6)
        self.N61.setObjectName(u"N61")
        self.N61.setMinimumSize(QSize(50, 0))
        self.N61.setMaximumSize(QSize(50, 16777215))
        self.N61.setMouseTracking(False)
        self.N61.setStyleSheet(u"")
        self.N61.setAlignment(Qt.AlignCenter)
        self.N61.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_87.addWidget(self.N61)

        self.horizontalSpacer_179 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_87.addItem(self.horizontalSpacer_179)

        self.N62 = QLineEdit(self.NO6)
        self.N62.setObjectName(u"N62")
        self.N62.setMinimumSize(QSize(50, 0))
        self.N62.setMaximumSize(QSize(50, 16777215))
        self.N62.setMouseTracking(False)
        self.N62.setStyleSheet(u"")
        self.N62.setAlignment(Qt.AlignCenter)
        self.N62.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_87.addWidget(self.N62)

        self.horizontalSpacer_180 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_87.addItem(self.horizontalSpacer_180)


        self.verticalLayout_24.addWidget(self.NO6)

        self.NO7 = QFrame(self.frame_3)
        self.NO7.setObjectName(u"NO7")
        self.NO7.setFrameShape(QFrame.StyledPanel)
        self.NO7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_86 = QHBoxLayout(self.NO7)
        self.horizontalLayout_86.setSpacing(0)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.horizontalLayout_86.setContentsMargins(0, 0, 0, 0)
        self.label_105 = QLabel(self.NO7)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setMaximumSize(QSize(110, 16777215))
        self.label_105.setFont(font6)
        self.label_105.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_86.addWidget(self.label_105)

        self.horizontalSpacer_175 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_86.addItem(self.horizontalSpacer_175)

        self.N71 = QLineEdit(self.NO7)
        self.N71.setObjectName(u"N71")
        self.N71.setMinimumSize(QSize(50, 0))
        self.N71.setMaximumSize(QSize(50, 16777215))
        self.N71.setMouseTracking(False)
        self.N71.setStyleSheet(u"")
        self.N71.setAlignment(Qt.AlignCenter)
        self.N71.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_86.addWidget(self.N71)

        self.horizontalSpacer_176 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_86.addItem(self.horizontalSpacer_176)

        self.N72 = QLineEdit(self.NO7)
        self.N72.setObjectName(u"N72")
        self.N72.setMinimumSize(QSize(50, 0))
        self.N72.setMaximumSize(QSize(50, 16777215))
        self.N72.setMouseTracking(False)
        self.N72.setStyleSheet(u"")
        self.N72.setAlignment(Qt.AlignCenter)
        self.N72.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_86.addWidget(self.N72)

        self.horizontalSpacer_177 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_86.addItem(self.horizontalSpacer_177)


        self.verticalLayout_24.addWidget(self.NO7)

        self.NO8 = QFrame(self.frame_3)
        self.NO8.setObjectName(u"NO8")
        self.NO8.setFrameShape(QFrame.StyledPanel)
        self.NO8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_85 = QHBoxLayout(self.NO8)
        self.horizontalLayout_85.setSpacing(0)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.horizontalLayout_85.setContentsMargins(0, 0, 0, 0)
        self.label_104 = QLabel(self.NO8)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setMaximumSize(QSize(110, 16777215))
        self.label_104.setFont(font6)
        self.label_104.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_85.addWidget(self.label_104)

        self.horizontalSpacer_172 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_85.addItem(self.horizontalSpacer_172)

        self.N81 = QLineEdit(self.NO8)
        self.N81.setObjectName(u"N81")
        self.N81.setMinimumSize(QSize(50, 0))
        self.N81.setMaximumSize(QSize(50, 16777215))
        self.N81.setMouseTracking(False)
        self.N81.setStyleSheet(u"")
        self.N81.setAlignment(Qt.AlignCenter)
        self.N81.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_85.addWidget(self.N81)

        self.horizontalSpacer_173 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_85.addItem(self.horizontalSpacer_173)

        self.N82 = QLineEdit(self.NO8)
        self.N82.setObjectName(u"N82")
        self.N82.setMinimumSize(QSize(50, 0))
        self.N82.setMaximumSize(QSize(50, 16777215))
        self.N82.setMouseTracking(False)
        self.N82.setStyleSheet(u"")
        self.N82.setAlignment(Qt.AlignCenter)
        self.N82.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_85.addWidget(self.N82)

        self.horizontalSpacer_174 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_85.addItem(self.horizontalSpacer_174)


        self.verticalLayout_24.addWidget(self.NO8)

        self.NO9 = QFrame(self.frame_3)
        self.NO9.setObjectName(u"NO9")
        self.NO9.setFrameShape(QFrame.StyledPanel)
        self.NO9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_79 = QHBoxLayout(self.NO9)
        self.horizontalLayout_79.setSpacing(0)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.horizontalLayout_79.setContentsMargins(0, 0, 0, 0)
        self.label_98 = QLabel(self.NO9)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setMaximumSize(QSize(110, 16777215))
        self.label_98.setFont(font6)
        self.label_98.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_79.addWidget(self.label_98)

        self.horizontalSpacer_154 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_79.addItem(self.horizontalSpacer_154)

        self.N91 = QLineEdit(self.NO9)
        self.N91.setObjectName(u"N91")
        self.N91.setMinimumSize(QSize(50, 0))
        self.N91.setMaximumSize(QSize(50, 16777215))
        self.N91.setMouseTracking(False)
        self.N91.setStyleSheet(u"")
        self.N91.setAlignment(Qt.AlignCenter)
        self.N91.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_79.addWidget(self.N91)

        self.horizontalSpacer_155 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_79.addItem(self.horizontalSpacer_155)

        self.N92 = QLineEdit(self.NO9)
        self.N92.setObjectName(u"N92")
        self.N92.setMinimumSize(QSize(50, 0))
        self.N92.setMaximumSize(QSize(50, 16777215))
        self.N92.setMouseTracking(False)
        self.N92.setStyleSheet(u"")
        self.N92.setAlignment(Qt.AlignCenter)
        self.N92.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_79.addWidget(self.N92)

        self.horizontalSpacer_156 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_79.addItem(self.horizontalSpacer_156)


        self.verticalLayout_24.addWidget(self.NO9)

        self.NO10 = QFrame(self.frame_3)
        self.NO10.setObjectName(u"NO10")
        self.NO10.setFrameShape(QFrame.StyledPanel)
        self.NO10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_81 = QHBoxLayout(self.NO10)
        self.horizontalLayout_81.setSpacing(0)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.horizontalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.label_100 = QLabel(self.NO10)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setMaximumSize(QSize(110, 16777215))
        self.label_100.setFont(font6)
        self.label_100.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_81.addWidget(self.label_100)

        self.horizontalSpacer_160 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_81.addItem(self.horizontalSpacer_160)

        self.N101 = QLineEdit(self.NO10)
        self.N101.setObjectName(u"N101")
        self.N101.setMinimumSize(QSize(50, 0))
        self.N101.setMaximumSize(QSize(50, 16777215))
        self.N101.setMouseTracking(False)
        self.N101.setStyleSheet(u"")
        self.N101.setAlignment(Qt.AlignCenter)
        self.N101.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_81.addWidget(self.N101)

        self.horizontalSpacer_161 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_81.addItem(self.horizontalSpacer_161)

        self.N102 = QLineEdit(self.NO10)
        self.N102.setObjectName(u"N102")
        self.N102.setMinimumSize(QSize(50, 0))
        self.N102.setMaximumSize(QSize(50, 16777215))
        self.N102.setMouseTracking(False)
        self.N102.setStyleSheet(u"")
        self.N102.setAlignment(Qt.AlignCenter)
        self.N102.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_81.addWidget(self.N102)

        self.horizontalSpacer_162 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_81.addItem(self.horizontalSpacer_162)


        self.verticalLayout_24.addWidget(self.NO10)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_4)


        self.horizontalLayout_111.addWidget(self.frame_3)

        self.frame_97 = QFrame(self.frame)
        self.frame_97.setObjectName(u"frame_97")
        self.frame_97.setFrameShape(QFrame.StyledPanel)
        self.frame_97.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_97)
        self.verticalLayout_26.setSpacing(8)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 5)
        self.frame_71 = QFrame(self.frame_97)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setMinimumSize(QSize(0, 40))
        self.frame_71.setMaximumSize(QSize(16777215, 40))
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_71)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_99 = QFrame(self.frame_71)
        self.frame_99.setObjectName(u"frame_99")
        self.frame_99.setFrameShape(QFrame.StyledPanel)
        self.frame_99.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_99)
        self.verticalLayout_27.setSpacing(3)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 10)
        self.frame_98 = QFrame(self.frame_99)
        self.frame_98.setObjectName(u"frame_98")
        self.frame_98.setFrameShape(QFrame.StyledPanel)
        self.frame_98.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_89 = QHBoxLayout(self.frame_98)
        self.horizontalLayout_89.setSpacing(50)
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.horizontalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.label_110 = QLabel(self.frame_98)
        self.label_110.setObjectName(u"label_110")
        self.label_110.setMaximumSize(QSize(50, 16777215))
        self.label_110.setFont(font5)
        self.label_110.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_89.addWidget(self.label_110)

        self.label_111 = QLabel(self.frame_98)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setMaximumSize(QSize(50, 16777215))
        self.label_111.setFont(font5)
        self.label_111.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_89.addWidget(self.label_111)

        self.label_112 = QLabel(self.frame_98)
        self.label_112.setObjectName(u"label_112")
        self.label_112.setMaximumSize(QSize(50, 16777215))
        self.label_112.setFont(font5)
        self.label_112.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_89.addWidget(self.label_112)


        self.verticalLayout_27.addWidget(self.frame_98)

        self.line_6 = QFrame(self.frame_99)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setMinimumSize(QSize(0, 2))
        self.line_6.setMaximumSize(QSize(16777215, 2))
        self.line_6.setStyleSheet(u"border: 1px solid rgb(0, 0, 0);")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_27.addWidget(self.line_6)


        self.verticalLayout_20.addWidget(self.frame_99)


        self.verticalLayout_26.addWidget(self.frame_71)

        self.NO11 = QFrame(self.frame_97)
        self.NO11.setObjectName(u"NO11")
        self.NO11.setFrameShape(QFrame.StyledPanel)
        self.NO11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_90 = QHBoxLayout(self.NO11)
        self.horizontalLayout_90.setSpacing(0)
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.horizontalLayout_90.setContentsMargins(0, 0, 0, 0)
        self.label_113 = QLabel(self.NO11)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setMaximumSize(QSize(110, 16777215))
        self.label_113.setFont(font6)
        self.label_113.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_90.addWidget(self.label_113)

        self.horizontalSpacer_181 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_90.addItem(self.horizontalSpacer_181)

        self.N111 = QLineEdit(self.NO11)
        self.N111.setObjectName(u"N111")
        self.N111.setMinimumSize(QSize(50, 0))
        self.N111.setMaximumSize(QSize(50, 16777215))
        self.N111.setMouseTracking(False)
        self.N111.setStyleSheet(u"")
        self.N111.setAlignment(Qt.AlignCenter)
        self.N111.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_90.addWidget(self.N111)

        self.horizontalSpacer_182 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_90.addItem(self.horizontalSpacer_182)

        self.N112 = QLineEdit(self.NO11)
        self.N112.setObjectName(u"N112")
        self.N112.setMinimumSize(QSize(50, 0))
        self.N112.setMaximumSize(QSize(50, 16777215))
        self.N112.setMouseTracking(False)
        self.N112.setStyleSheet(u"")
        self.N112.setAlignment(Qt.AlignCenter)
        self.N112.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_90.addWidget(self.N112)

        self.horizontalSpacer_183 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_90.addItem(self.horizontalSpacer_183)


        self.verticalLayout_26.addWidget(self.NO11)

        self.NO12 = QFrame(self.frame_97)
        self.NO12.setObjectName(u"NO12")
        self.NO12.setFrameShape(QFrame.StyledPanel)
        self.NO12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_91 = QHBoxLayout(self.NO12)
        self.horizontalLayout_91.setSpacing(0)
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.horizontalLayout_91.setContentsMargins(0, 0, 0, 0)
        self.label_114 = QLabel(self.NO12)
        self.label_114.setObjectName(u"label_114")
        self.label_114.setMaximumSize(QSize(110, 16777215))
        self.label_114.setFont(font6)
        self.label_114.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_91.addWidget(self.label_114)

        self.horizontalSpacer_184 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_91.addItem(self.horizontalSpacer_184)

        self.N121 = QLineEdit(self.NO12)
        self.N121.setObjectName(u"N121")
        self.N121.setMinimumSize(QSize(50, 0))
        self.N121.setMaximumSize(QSize(50, 16777215))
        self.N121.setMouseTracking(False)
        self.N121.setStyleSheet(u"")
        self.N121.setAlignment(Qt.AlignCenter)
        self.N121.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_91.addWidget(self.N121)

        self.horizontalSpacer_185 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_91.addItem(self.horizontalSpacer_185)

        self.N122 = QLineEdit(self.NO12)
        self.N122.setObjectName(u"N122")
        self.N122.setMinimumSize(QSize(50, 0))
        self.N122.setMaximumSize(QSize(50, 16777215))
        self.N122.setMouseTracking(False)
        self.N122.setStyleSheet(u"")
        self.N122.setAlignment(Qt.AlignCenter)
        self.N122.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_91.addWidget(self.N122)

        self.horizontalSpacer_186 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_91.addItem(self.horizontalSpacer_186)


        self.verticalLayout_26.addWidget(self.NO12)

        self.NO13 = QFrame(self.frame_97)
        self.NO13.setObjectName(u"NO13")
        self.NO13.setFrameShape(QFrame.StyledPanel)
        self.NO13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_92 = QHBoxLayout(self.NO13)
        self.horizontalLayout_92.setSpacing(0)
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.horizontalLayout_92.setContentsMargins(0, 0, 0, 0)
        self.label_115 = QLabel(self.NO13)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setMaximumSize(QSize(110, 16777215))
        self.label_115.setFont(font6)
        self.label_115.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_92.addWidget(self.label_115)

        self.horizontalSpacer_187 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_92.addItem(self.horizontalSpacer_187)

        self.N131 = QLineEdit(self.NO13)
        self.N131.setObjectName(u"N131")
        self.N131.setMinimumSize(QSize(50, 0))
        self.N131.setMaximumSize(QSize(50, 16777215))
        self.N131.setMouseTracking(False)
        self.N131.setStyleSheet(u"")
        self.N131.setAlignment(Qt.AlignCenter)
        self.N131.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_92.addWidget(self.N131)

        self.horizontalSpacer_188 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_92.addItem(self.horizontalSpacer_188)

        self.N132 = QLineEdit(self.NO13)
        self.N132.setObjectName(u"N132")
        self.N132.setMinimumSize(QSize(50, 0))
        self.N132.setMaximumSize(QSize(50, 16777215))
        self.N132.setMouseTracking(False)
        self.N132.setStyleSheet(u"")
        self.N132.setAlignment(Qt.AlignCenter)
        self.N132.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_92.addWidget(self.N132)

        self.horizontalSpacer_189 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_92.addItem(self.horizontalSpacer_189)


        self.verticalLayout_26.addWidget(self.NO13)

        self.NO14 = QFrame(self.frame_97)
        self.NO14.setObjectName(u"NO14")
        self.NO14.setFrameShape(QFrame.StyledPanel)
        self.NO14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_93 = QHBoxLayout(self.NO14)
        self.horizontalLayout_93.setSpacing(0)
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.horizontalLayout_93.setContentsMargins(0, 0, 0, 0)
        self.label_116 = QLabel(self.NO14)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setMaximumSize(QSize(110, 16777215))
        self.label_116.setFont(font6)
        self.label_116.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_93.addWidget(self.label_116)

        self.horizontalSpacer_190 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_93.addItem(self.horizontalSpacer_190)

        self.N141 = QLineEdit(self.NO14)
        self.N141.setObjectName(u"N141")
        self.N141.setMinimumSize(QSize(50, 0))
        self.N141.setMaximumSize(QSize(50, 16777215))
        self.N141.setMouseTracking(False)
        self.N141.setStyleSheet(u"")
        self.N141.setAlignment(Qt.AlignCenter)
        self.N141.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_93.addWidget(self.N141)

        self.horizontalSpacer_191 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_93.addItem(self.horizontalSpacer_191)

        self.N142 = QLineEdit(self.NO14)
        self.N142.setObjectName(u"N142")
        self.N142.setMinimumSize(QSize(50, 0))
        self.N142.setMaximumSize(QSize(50, 16777215))
        self.N142.setMouseTracking(False)
        self.N142.setStyleSheet(u"")
        self.N142.setAlignment(Qt.AlignCenter)
        self.N142.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_93.addWidget(self.N142)

        self.horizontalSpacer_192 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_93.addItem(self.horizontalSpacer_192)


        self.verticalLayout_26.addWidget(self.NO14)

        self.NO15 = QFrame(self.frame_97)
        self.NO15.setObjectName(u"NO15")
        self.NO15.setFrameShape(QFrame.StyledPanel)
        self.NO15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_94 = QHBoxLayout(self.NO15)
        self.horizontalLayout_94.setSpacing(0)
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.horizontalLayout_94.setContentsMargins(0, 0, 0, 0)
        self.label_117 = QLabel(self.NO15)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setMaximumSize(QSize(110, 16777215))
        self.label_117.setFont(font6)
        self.label_117.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_94.addWidget(self.label_117)

        self.horizontalSpacer_193 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_94.addItem(self.horizontalSpacer_193)

        self.N151 = QLineEdit(self.NO15)
        self.N151.setObjectName(u"N151")
        self.N151.setMinimumSize(QSize(50, 0))
        self.N151.setMaximumSize(QSize(50, 16777215))
        self.N151.setMouseTracking(False)
        self.N151.setStyleSheet(u"")
        self.N151.setAlignment(Qt.AlignCenter)
        self.N151.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_94.addWidget(self.N151)

        self.horizontalSpacer_194 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_94.addItem(self.horizontalSpacer_194)

        self.N152 = QLineEdit(self.NO15)
        self.N152.setObjectName(u"N152")
        self.N152.setMinimumSize(QSize(50, 0))
        self.N152.setMaximumSize(QSize(50, 16777215))
        self.N152.setMouseTracking(False)
        self.N152.setStyleSheet(u"")
        self.N152.setAlignment(Qt.AlignCenter)
        self.N152.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_94.addWidget(self.N152)

        self.horizontalSpacer_195 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_94.addItem(self.horizontalSpacer_195)


        self.verticalLayout_26.addWidget(self.NO15)

        self.NO16 = QFrame(self.frame_97)
        self.NO16.setObjectName(u"NO16")
        self.NO16.setFrameShape(QFrame.StyledPanel)
        self.NO16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_95 = QHBoxLayout(self.NO16)
        self.horizontalLayout_95.setSpacing(0)
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.horizontalLayout_95.setContentsMargins(0, 0, 0, 0)
        self.label_118 = QLabel(self.NO16)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setMaximumSize(QSize(110, 16777215))
        self.label_118.setFont(font6)
        self.label_118.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_95.addWidget(self.label_118)

        self.horizontalSpacer_196 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_95.addItem(self.horizontalSpacer_196)

        self.N161 = QLineEdit(self.NO16)
        self.N161.setObjectName(u"N161")
        self.N161.setMinimumSize(QSize(50, 0))
        self.N161.setMaximumSize(QSize(50, 16777215))
        self.N161.setMouseTracking(False)
        self.N161.setStyleSheet(u"")
        self.N161.setAlignment(Qt.AlignCenter)
        self.N161.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_95.addWidget(self.N161)

        self.horizontalSpacer_197 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_95.addItem(self.horizontalSpacer_197)

        self.N162 = QLineEdit(self.NO16)
        self.N162.setObjectName(u"N162")
        self.N162.setMinimumSize(QSize(50, 0))
        self.N162.setMaximumSize(QSize(50, 16777215))
        self.N162.setMouseTracking(False)
        self.N162.setStyleSheet(u"")
        self.N162.setAlignment(Qt.AlignCenter)
        self.N162.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_95.addWidget(self.N162)

        self.horizontalSpacer_198 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_95.addItem(self.horizontalSpacer_198)


        self.verticalLayout_26.addWidget(self.NO16)

        self.NO17 = QFrame(self.frame_97)
        self.NO17.setObjectName(u"NO17")
        self.NO17.setFrameShape(QFrame.StyledPanel)
        self.NO17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_96 = QHBoxLayout(self.NO17)
        self.horizontalLayout_96.setSpacing(0)
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.horizontalLayout_96.setContentsMargins(0, 0, 0, 0)
        self.label_119 = QLabel(self.NO17)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setMaximumSize(QSize(110, 16777215))
        self.label_119.setFont(font6)
        self.label_119.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_96.addWidget(self.label_119)

        self.horizontalSpacer_199 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_96.addItem(self.horizontalSpacer_199)

        self.N171 = QLineEdit(self.NO17)
        self.N171.setObjectName(u"N171")
        self.N171.setMinimumSize(QSize(50, 0))
        self.N171.setMaximumSize(QSize(50, 16777215))
        self.N171.setMouseTracking(False)
        self.N171.setStyleSheet(u"")
        self.N171.setAlignment(Qt.AlignCenter)
        self.N171.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_96.addWidget(self.N171)

        self.horizontalSpacer_200 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_96.addItem(self.horizontalSpacer_200)

        self.N172 = QLineEdit(self.NO17)
        self.N172.setObjectName(u"N172")
        self.N172.setMinimumSize(QSize(50, 0))
        self.N172.setMaximumSize(QSize(50, 16777215))
        self.N172.setMouseTracking(False)
        self.N172.setStyleSheet(u"")
        self.N172.setAlignment(Qt.AlignCenter)
        self.N172.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_96.addWidget(self.N172)

        self.horizontalSpacer_201 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_96.addItem(self.horizontalSpacer_201)


        self.verticalLayout_26.addWidget(self.NO17)

        self.NO18 = QFrame(self.frame_97)
        self.NO18.setObjectName(u"NO18")
        self.NO18.setFrameShape(QFrame.StyledPanel)
        self.NO18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_97 = QHBoxLayout(self.NO18)
        self.horizontalLayout_97.setSpacing(0)
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.horizontalLayout_97.setContentsMargins(0, 0, 0, 0)
        self.label_120 = QLabel(self.NO18)
        self.label_120.setObjectName(u"label_120")
        self.label_120.setMaximumSize(QSize(110, 16777215))
        self.label_120.setFont(font6)
        self.label_120.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_97.addWidget(self.label_120)

        self.horizontalSpacer_202 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_97.addItem(self.horizontalSpacer_202)

        self.N181 = QLineEdit(self.NO18)
        self.N181.setObjectName(u"N181")
        self.N181.setMinimumSize(QSize(50, 0))
        self.N181.setMaximumSize(QSize(50, 16777215))
        self.N181.setMouseTracking(False)
        self.N181.setStyleSheet(u"")
        self.N181.setAlignment(Qt.AlignCenter)
        self.N181.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_97.addWidget(self.N181)

        self.horizontalSpacer_203 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_97.addItem(self.horizontalSpacer_203)

        self.N182 = QLineEdit(self.NO18)
        self.N182.setObjectName(u"N182")
        self.N182.setMinimumSize(QSize(50, 0))
        self.N182.setMaximumSize(QSize(50, 16777215))
        self.N182.setMouseTracking(False)
        self.N182.setStyleSheet(u"")
        self.N182.setAlignment(Qt.AlignCenter)
        self.N182.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_97.addWidget(self.N182)

        self.horizontalSpacer_204 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_97.addItem(self.horizontalSpacer_204)


        self.verticalLayout_26.addWidget(self.NO18)

        self.NO19 = QFrame(self.frame_97)
        self.NO19.setObjectName(u"NO19")
        self.NO19.setFrameShape(QFrame.StyledPanel)
        self.NO19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_98 = QHBoxLayout(self.NO19)
        self.horizontalLayout_98.setSpacing(0)
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.horizontalLayout_98.setContentsMargins(0, 0, 0, 0)
        self.label_121 = QLabel(self.NO19)
        self.label_121.setObjectName(u"label_121")
        self.label_121.setMaximumSize(QSize(110, 16777215))
        self.label_121.setFont(font6)
        self.label_121.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_98.addWidget(self.label_121)

        self.horizontalSpacer_205 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_98.addItem(self.horizontalSpacer_205)

        self.N191 = QLineEdit(self.NO19)
        self.N191.setObjectName(u"N191")
        self.N191.setMinimumSize(QSize(50, 0))
        self.N191.setMaximumSize(QSize(50, 16777215))
        self.N191.setMouseTracking(False)
        self.N191.setStyleSheet(u"")
        self.N191.setAlignment(Qt.AlignCenter)
        self.N191.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_98.addWidget(self.N191)

        self.horizontalSpacer_206 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_98.addItem(self.horizontalSpacer_206)

        self.N192 = QLineEdit(self.NO19)
        self.N192.setObjectName(u"N192")
        self.N192.setMinimumSize(QSize(50, 0))
        self.N192.setMaximumSize(QSize(50, 16777215))
        self.N192.setMouseTracking(False)
        self.N192.setStyleSheet(u"")
        self.N192.setAlignment(Qt.AlignCenter)
        self.N192.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_98.addWidget(self.N192)

        self.horizontalSpacer_207 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_98.addItem(self.horizontalSpacer_207)


        self.verticalLayout_26.addWidget(self.NO19)

        self.NO20 = QFrame(self.frame_97)
        self.NO20.setObjectName(u"NO20")
        self.NO20.setFrameShape(QFrame.StyledPanel)
        self.NO20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_99 = QHBoxLayout(self.NO20)
        self.horizontalLayout_99.setSpacing(0)
        self.horizontalLayout_99.setObjectName(u"horizontalLayout_99")
        self.horizontalLayout_99.setContentsMargins(0, 0, 0, 0)
        self.label_122 = QLabel(self.NO20)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setMaximumSize(QSize(110, 16777215))
        self.label_122.setFont(font6)
        self.label_122.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_99.addWidget(self.label_122)

        self.horizontalSpacer_208 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_99.addItem(self.horizontalSpacer_208)

        self.N201 = QLineEdit(self.NO20)
        self.N201.setObjectName(u"N201")
        self.N201.setMinimumSize(QSize(50, 0))
        self.N201.setMaximumSize(QSize(50, 16777215))
        self.N201.setMouseTracking(False)
        self.N201.setStyleSheet(u"")
        self.N201.setAlignment(Qt.AlignCenter)
        self.N201.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_99.addWidget(self.N201)

        self.horizontalSpacer_209 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_99.addItem(self.horizontalSpacer_209)

        self.N202 = QLineEdit(self.NO20)
        self.N202.setObjectName(u"N202")
        self.N202.setMinimumSize(QSize(50, 0))
        self.N202.setMaximumSize(QSize(50, 16777215))
        self.N202.setMouseTracking(False)
        self.N202.setStyleSheet(u"")
        self.N202.setAlignment(Qt.AlignCenter)
        self.N202.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_99.addWidget(self.N202)

        self.horizontalSpacer_210 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_99.addItem(self.horizontalSpacer_210)


        self.verticalLayout_26.addWidget(self.NO20)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer_3)


        self.horizontalLayout_111.addWidget(self.frame_97)


        self.verticalLayout_10.addWidget(self.frame)

        self.frame_23 = QFrame(self.frame_16)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.NoFrame)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, 25, -1, -1)
        self.nextButtonNo = QPushButton(self.frame_23)
        self.nextButtonNo.setObjectName(u"nextButtonNo")
        self.nextButtonNo.setMinimumSize(QSize(0, 30))
        self.nextButtonNo.setMaximumSize(QSize(150, 16777215))
        self.nextButtonNo.setFont(font4)
        self.nextButtonNo.setStyleSheet(u"QPushButton {\n"
"	padding-left: 5px;\n"
"	background-color: rgb(38, 40, 61);\n"
"	border:none;\n"
"	border-radius:15px;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 3px solid;\n"
"	background-color:rgb(241, 102, 55);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color:rgb(241, 102, 55);\n"
"}\n"
"")

        self.horizontalLayout_15.addWidget(self.nextButtonNo)


        self.verticalLayout_10.addWidget(self.frame_23)


        self.verticalLayout_8.addWidget(self.frame_16)


        self.horizontalLayout_16.addWidget(self.frame_14)

        self.stackedWidget.addWidget(self.Nos)
        self.Elementos = QWidget()
        self.Elementos.setObjectName(u"Elementos")
        self.horizontalLayout_9 = QHBoxLayout(self.Elementos)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_17 = QFrame(self.Elementos)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(900, 700))
        self.frame_17.setFont(font)
        self.frame_17.setStyleSheet(u"QFrame{\n"
"background-color: rgb(148, 147, 150);\n"
"border-radius: 6px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: rgb(217, 217, 217);\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 5px;\n"
"    padding: 0px;\n"
"    font-size: 14px;\n"
"    color: #333;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color: rgb(217, 217, 217);\n"
"    border: 1px solid #66afe9;\n"
"    outline: none;\n"
"}")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_17)
        self.verticalLayout_11.setSpacing(7)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_26 = QFrame(self.frame_17)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMaximumSize(QSize(16777215, 40))
        self.frame_26.setFont(font1)
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_26)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_11 = QLabel(self.frame_26)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_11)


        self.verticalLayout_11.addWidget(self.frame_26)

        self.frame_18 = QFrame(self.frame_17)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid rgb(38, 40, 61);\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_10.setSpacing(30)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.frame_18)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_20)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 5)
        self.frame_name = QFrame(self.frame_20)
        self.frame_name.setObjectName(u"frame_name")
        self.frame_name.setMinimumSize(QSize(0, 40))
        self.frame_name.setMaximumSize(QSize(16777215, 40))
        self.frame_name.setFrameShape(QFrame.StyledPanel)
        self.frame_name.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_name)
        self.verticalLayout_15.setSpacing(3)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 10)
        self.frame_34 = QFrame(self.frame_name)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_18.setSpacing(50)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(25, 0, 32, 0)
        self.label_28 = QLabel(self.frame_34)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMaximumSize(QSize(90, 16777215))
        self.label_28.setFont(font5)
        self.label_28.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_28)

        self.label_31 = QLabel(self.frame_34)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMaximumSize(QSize(100, 16777215))
        self.label_31.setFont(font5)
        self.label_31.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_31)

        self.label_42 = QLabel(self.frame_34)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMaximumSize(QSize(100, 16777215))
        self.label_42.setFont(font5)
        self.label_42.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_42)


        self.verticalLayout_15.addWidget(self.frame_34)

        self.line_2 = QFrame(self.frame_name)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(0, 2))
        self.line_2.setMaximumSize(QSize(16777215, 2))
        self.line_2.setStyleSheet(u"border: 1px solid rgb(0, 0, 0);")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_15.addWidget(self.line_2)


        self.verticalLayout_30.addWidget(self.frame_name)

        self.EL1 = QFrame(self.frame_20)
        self.EL1.setObjectName(u"EL1")
        self.EL1.setMinimumSize(QSize(0, 26))
        self.EL1.setFrameShape(QFrame.StyledPanel)
        self.EL1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.EL1)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_43 = QLabel(self.EL1)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMaximumSize(QSize(110, 16777215))
        self.label_43.setFont(font6)
        self.label_43.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_43)

        self.horizontalSpacer_40 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_40)

        self.E11 = QLineEdit(self.EL1)
        self.E11.setObjectName(u"E11")
        self.E11.setMinimumSize(QSize(50, 0))
        self.E11.setMaximumSize(QSize(50, 16777215))
        self.E11.setMouseTracking(False)
        self.E11.setStyleSheet(u"")
        self.E11.setAlignment(Qt.AlignCenter)
        self.E11.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_24.addWidget(self.E11)

        self.horizontalSpacer_41 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_41)

        self.E12 = QLineEdit(self.EL1)
        self.E12.setObjectName(u"E12")
        self.E12.setMinimumSize(QSize(50, 0))
        self.E12.setMaximumSize(QSize(50, 16777215))
        self.E12.setMouseTracking(False)
        self.E12.setStyleSheet(u"")
        self.E12.setAlignment(Qt.AlignCenter)
        self.E12.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_24.addWidget(self.E12)

        self.horizontalSpacer_42 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_42)


        self.verticalLayout_30.addWidget(self.EL1)

        self.EL2 = QFrame(self.frame_20)
        self.EL2.setObjectName(u"EL2")
        self.EL2.setMinimumSize(QSize(0, 26))
        self.EL2.setFrameShape(QFrame.StyledPanel)
        self.EL2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.EL2)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_44 = QLabel(self.EL2)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMaximumSize(QSize(110, 16777215))
        self.label_44.setFont(font6)
        self.label_44.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.label_44)

        self.horizontalSpacer_43 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_43)

        self.E21 = QLineEdit(self.EL2)
        self.E21.setObjectName(u"E21")
        self.E21.setMinimumSize(QSize(50, 0))
        self.E21.setMaximumSize(QSize(50, 16777215))
        self.E21.setMouseTracking(False)
        self.E21.setStyleSheet(u"")
        self.E21.setAlignment(Qt.AlignCenter)
        self.E21.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_25.addWidget(self.E21)

        self.horizontalSpacer_44 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_44)

        self.E22 = QLineEdit(self.EL2)
        self.E22.setObjectName(u"E22")
        self.E22.setMinimumSize(QSize(50, 0))
        self.E22.setMaximumSize(QSize(50, 16777215))
        self.E22.setMouseTracking(False)
        self.E22.setStyleSheet(u"")
        self.E22.setAlignment(Qt.AlignCenter)
        self.E22.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_25.addWidget(self.E22)

        self.horizontalSpacer_45 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_45)


        self.verticalLayout_30.addWidget(self.EL2)

        self.EL3 = QFrame(self.frame_20)
        self.EL3.setObjectName(u"EL3")
        self.EL3.setMinimumSize(QSize(0, 26))
        self.EL3.setFrameShape(QFrame.StyledPanel)
        self.EL3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.EL3)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_45 = QLabel(self.EL3)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMaximumSize(QSize(110, 16777215))
        self.label_45.setFont(font6)
        self.label_45.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.label_45)

        self.horizontalSpacer_46 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_46)

        self.E31 = QLineEdit(self.EL3)
        self.E31.setObjectName(u"E31")
        self.E31.setMinimumSize(QSize(50, 0))
        self.E31.setMaximumSize(QSize(50, 16777215))
        self.E31.setMouseTracking(False)
        self.E31.setStyleSheet(u"")
        self.E31.setAlignment(Qt.AlignCenter)
        self.E31.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_26.addWidget(self.E31)

        self.horizontalSpacer_47 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_47)

        self.E32 = QLineEdit(self.EL3)
        self.E32.setObjectName(u"E32")
        self.E32.setMinimumSize(QSize(50, 0))
        self.E32.setMaximumSize(QSize(50, 16777215))
        self.E32.setMouseTracking(False)
        self.E32.setStyleSheet(u"")
        self.E32.setAlignment(Qt.AlignCenter)
        self.E32.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_26.addWidget(self.E32)

        self.horizontalSpacer_48 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_48)


        self.verticalLayout_30.addWidget(self.EL3)

        self.EL4 = QFrame(self.frame_20)
        self.EL4.setObjectName(u"EL4")
        self.EL4.setMinimumSize(QSize(0, 26))
        self.EL4.setFrameShape(QFrame.StyledPanel)
        self.EL4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.EL4)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.label_46 = QLabel(self.EL4)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMaximumSize(QSize(110, 16777215))
        self.label_46.setFont(font6)
        self.label_46.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.label_46)

        self.horizontalSpacer_49 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_49)

        self.E41 = QLineEdit(self.EL4)
        self.E41.setObjectName(u"E41")
        self.E41.setMinimumSize(QSize(50, 0))
        self.E41.setMaximumSize(QSize(50, 16777215))
        self.E41.setMouseTracking(False)
        self.E41.setStyleSheet(u"")
        self.E41.setAlignment(Qt.AlignCenter)
        self.E41.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_27.addWidget(self.E41)

        self.horizontalSpacer_50 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_50)

        self.E42 = QLineEdit(self.EL4)
        self.E42.setObjectName(u"E42")
        self.E42.setMinimumSize(QSize(50, 0))
        self.E42.setMaximumSize(QSize(50, 16777215))
        self.E42.setMouseTracking(False)
        self.E42.setStyleSheet(u"")
        self.E42.setAlignment(Qt.AlignCenter)
        self.E42.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_27.addWidget(self.E42)

        self.horizontalSpacer_51 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_51)


        self.verticalLayout_30.addWidget(self.EL4)

        self.EL5 = QFrame(self.frame_20)
        self.EL5.setObjectName(u"EL5")
        self.EL5.setMinimumSize(QSize(0, 26))
        self.EL5.setFrameShape(QFrame.StyledPanel)
        self.EL5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.EL5)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.label_47 = QLabel(self.EL5)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMaximumSize(QSize(110, 16777215))
        self.label_47.setFont(font6)
        self.label_47.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.label_47)

        self.horizontalSpacer_52 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_52)

        self.E51 = QLineEdit(self.EL5)
        self.E51.setObjectName(u"E51")
        self.E51.setMinimumSize(QSize(50, 0))
        self.E51.setMaximumSize(QSize(50, 16777215))
        self.E51.setMouseTracking(False)
        self.E51.setStyleSheet(u"")
        self.E51.setAlignment(Qt.AlignCenter)
        self.E51.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_28.addWidget(self.E51)

        self.horizontalSpacer_53 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_53)

        self.E52 = QLineEdit(self.EL5)
        self.E52.setObjectName(u"E52")
        self.E52.setMinimumSize(QSize(50, 0))
        self.E52.setMaximumSize(QSize(50, 16777215))
        self.E52.setMouseTracking(False)
        self.E52.setStyleSheet(u"")
        self.E52.setAlignment(Qt.AlignCenter)
        self.E52.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_28.addWidget(self.E52)

        self.horizontalSpacer_54 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_54)


        self.verticalLayout_30.addWidget(self.EL5)

        self.EL6 = QFrame(self.frame_20)
        self.EL6.setObjectName(u"EL6")
        self.EL6.setMinimumSize(QSize(0, 26))
        self.EL6.setFrameShape(QFrame.StyledPanel)
        self.EL6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.EL6)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_48 = QLabel(self.EL6)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMaximumSize(QSize(110, 16777215))
        self.label_48.setFont(font6)
        self.label_48.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.label_48)

        self.horizontalSpacer_55 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_55)

        self.E61 = QLineEdit(self.EL6)
        self.E61.setObjectName(u"E61")
        self.E61.setMinimumSize(QSize(50, 0))
        self.E61.setMaximumSize(QSize(50, 16777215))
        self.E61.setMouseTracking(False)
        self.E61.setStyleSheet(u"")
        self.E61.setAlignment(Qt.AlignCenter)
        self.E61.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_29.addWidget(self.E61)

        self.horizontalSpacer_56 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_56)

        self.E62 = QLineEdit(self.EL6)
        self.E62.setObjectName(u"E62")
        self.E62.setMinimumSize(QSize(50, 0))
        self.E62.setMaximumSize(QSize(50, 16777215))
        self.E62.setMouseTracking(False)
        self.E62.setStyleSheet(u"")
        self.E62.setAlignment(Qt.AlignCenter)
        self.E62.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_29.addWidget(self.E62)

        self.horizontalSpacer_57 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_57)


        self.verticalLayout_30.addWidget(self.EL6)

        self.EL7 = QFrame(self.frame_20)
        self.EL7.setObjectName(u"EL7")
        self.EL7.setMinimumSize(QSize(0, 26))
        self.EL7.setFrameShape(QFrame.StyledPanel)
        self.EL7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.EL7)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label_49 = QLabel(self.EL7)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMaximumSize(QSize(110, 16777215))
        self.label_49.setFont(font6)
        self.label_49.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_30.addWidget(self.label_49)

        self.horizontalSpacer_58 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_58)

        self.E71 = QLineEdit(self.EL7)
        self.E71.setObjectName(u"E71")
        self.E71.setMinimumSize(QSize(50, 0))
        self.E71.setMaximumSize(QSize(50, 16777215))
        self.E71.setMouseTracking(False)
        self.E71.setStyleSheet(u"")
        self.E71.setAlignment(Qt.AlignCenter)
        self.E71.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_30.addWidget(self.E71)

        self.horizontalSpacer_59 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_59)

        self.E72 = QLineEdit(self.EL7)
        self.E72.setObjectName(u"E72")
        self.E72.setMinimumSize(QSize(50, 0))
        self.E72.setMaximumSize(QSize(50, 16777215))
        self.E72.setMouseTracking(False)
        self.E72.setStyleSheet(u"")
        self.E72.setAlignment(Qt.AlignCenter)
        self.E72.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_30.addWidget(self.E72)

        self.horizontalSpacer_60 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_60)


        self.verticalLayout_30.addWidget(self.EL7)

        self.EL8 = QFrame(self.frame_20)
        self.EL8.setObjectName(u"EL8")
        self.EL8.setMinimumSize(QSize(0, 26))
        self.EL8.setFrameShape(QFrame.StyledPanel)
        self.EL8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.EL8)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.label_50 = QLabel(self.EL8)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMaximumSize(QSize(110, 16777215))
        self.label_50.setFont(font6)
        self.label_50.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_31.addWidget(self.label_50)

        self.horizontalSpacer_61 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_61)

        self.E81 = QLineEdit(self.EL8)
        self.E81.setObjectName(u"E81")
        self.E81.setMinimumSize(QSize(50, 0))
        self.E81.setMaximumSize(QSize(50, 16777215))
        self.E81.setMouseTracking(False)
        self.E81.setStyleSheet(u"")
        self.E81.setAlignment(Qt.AlignCenter)
        self.E81.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_31.addWidget(self.E81)

        self.horizontalSpacer_62 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_62)

        self.E82 = QLineEdit(self.EL8)
        self.E82.setObjectName(u"E82")
        self.E82.setMinimumSize(QSize(50, 0))
        self.E82.setMaximumSize(QSize(50, 16777215))
        self.E82.setMouseTracking(False)
        self.E82.setStyleSheet(u"")
        self.E82.setAlignment(Qt.AlignCenter)
        self.E82.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_31.addWidget(self.E82)

        self.horizontalSpacer_63 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_63)


        self.verticalLayout_30.addWidget(self.EL8)

        self.EL9 = QFrame(self.frame_20)
        self.EL9.setObjectName(u"EL9")
        self.EL9.setMinimumSize(QSize(0, 26))
        self.EL9.setFrameShape(QFrame.StyledPanel)
        self.EL9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.EL9)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.label_51 = QLabel(self.EL9)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMaximumSize(QSize(110, 16777215))
        self.label_51.setFont(font6)
        self.label_51.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.label_51)

        self.horizontalSpacer_64 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_64)

        self.E91 = QLineEdit(self.EL9)
        self.E91.setObjectName(u"E91")
        self.E91.setMinimumSize(QSize(50, 0))
        self.E91.setMaximumSize(QSize(50, 16777215))
        self.E91.setMouseTracking(False)
        self.E91.setStyleSheet(u"")
        self.E91.setAlignment(Qt.AlignCenter)
        self.E91.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_32.addWidget(self.E91)

        self.horizontalSpacer_65 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_65)

        self.E92 = QLineEdit(self.EL9)
        self.E92.setObjectName(u"E92")
        self.E92.setMinimumSize(QSize(50, 0))
        self.E92.setMaximumSize(QSize(50, 16777215))
        self.E92.setMouseTracking(False)
        self.E92.setStyleSheet(u"")
        self.E92.setAlignment(Qt.AlignCenter)
        self.E92.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_32.addWidget(self.E92)

        self.horizontalSpacer_66 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_66)


        self.verticalLayout_30.addWidget(self.EL9)

        self.EL10 = QFrame(self.frame_20)
        self.EL10.setObjectName(u"EL10")
        self.EL10.setMinimumSize(QSize(0, 26))
        self.EL10.setFrameShape(QFrame.StyledPanel)
        self.EL10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.EL10)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.label_52 = QLabel(self.EL10)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMaximumSize(QSize(110, 16777215))
        self.label_52.setFont(font6)
        self.label_52.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_33.addWidget(self.label_52)

        self.horizontalSpacer_67 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_67)

        self.E101 = QLineEdit(self.EL10)
        self.E101.setObjectName(u"E101")
        self.E101.setMinimumSize(QSize(50, 0))
        self.E101.setMaximumSize(QSize(50, 16777215))
        self.E101.setMouseTracking(False)
        self.E101.setStyleSheet(u"")
        self.E101.setAlignment(Qt.AlignCenter)
        self.E101.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_33.addWidget(self.E101)

        self.horizontalSpacer_68 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_68)

        self.E102 = QLineEdit(self.EL10)
        self.E102.setObjectName(u"E102")
        self.E102.setMinimumSize(QSize(50, 0))
        self.E102.setMaximumSize(QSize(50, 16777215))
        self.E102.setMouseTracking(False)
        self.E102.setStyleSheet(u"")
        self.E102.setAlignment(Qt.AlignCenter)
        self.E102.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_33.addWidget(self.E102)

        self.horizontalSpacer_69 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_69)


        self.verticalLayout_30.addWidget(self.EL10)

        self.EL11 = QFrame(self.frame_20)
        self.EL11.setObjectName(u"EL11")
        self.EL11.setMinimumSize(QSize(0, 26))
        self.EL11.setFrameShape(QFrame.StyledPanel)
        self.EL11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.EL11)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.label_53 = QLabel(self.EL11)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setMaximumSize(QSize(110, 16777215))
        self.label_53.setFont(font6)
        self.label_53.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.label_53)

        self.horizontalSpacer_70 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_70)

        self.E111 = QLineEdit(self.EL11)
        self.E111.setObjectName(u"E111")
        self.E111.setMinimumSize(QSize(50, 0))
        self.E111.setMaximumSize(QSize(50, 16777215))
        self.E111.setMouseTracking(False)
        self.E111.setStyleSheet(u"")
        self.E111.setAlignment(Qt.AlignCenter)
        self.E111.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_35.addWidget(self.E111)

        self.horizontalSpacer_71 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_71)

        self.E112 = QLineEdit(self.EL11)
        self.E112.setObjectName(u"E112")
        self.E112.setMinimumSize(QSize(50, 0))
        self.E112.setMaximumSize(QSize(50, 16777215))
        self.E112.setMouseTracking(False)
        self.E112.setStyleSheet(u"")
        self.E112.setAlignment(Qt.AlignCenter)
        self.E112.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_35.addWidget(self.E112)

        self.horizontalSpacer_72 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_72)


        self.verticalLayout_30.addWidget(self.EL11)

        self.EL12 = QFrame(self.frame_20)
        self.EL12.setObjectName(u"EL12")
        self.EL12.setMinimumSize(QSize(0, 26))
        self.EL12.setFrameShape(QFrame.StyledPanel)
        self.EL12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.EL12)
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.label_57 = QLabel(self.EL12)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMaximumSize(QSize(110, 16777215))
        self.label_57.setFont(font6)
        self.label_57.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_39.addWidget(self.label_57)

        self.horizontalSpacer_82 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_82)

        self.E121 = QLineEdit(self.EL12)
        self.E121.setObjectName(u"E121")
        self.E121.setMinimumSize(QSize(50, 0))
        self.E121.setMaximumSize(QSize(50, 16777215))
        self.E121.setMouseTracking(False)
        self.E121.setStyleSheet(u"")
        self.E121.setAlignment(Qt.AlignCenter)
        self.E121.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_39.addWidget(self.E121)

        self.horizontalSpacer_83 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_83)

        self.E122 = QLineEdit(self.EL12)
        self.E122.setObjectName(u"E122")
        self.E122.setMinimumSize(QSize(50, 0))
        self.E122.setMaximumSize(QSize(50, 16777215))
        self.E122.setMouseTracking(False)
        self.E122.setStyleSheet(u"")
        self.E122.setAlignment(Qt.AlignCenter)
        self.E122.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_39.addWidget(self.E122)

        self.horizontalSpacer_84 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_84)


        self.verticalLayout_30.addWidget(self.EL12)

        self.EL13 = QFrame(self.frame_20)
        self.EL13.setObjectName(u"EL13")
        self.EL13.setMinimumSize(QSize(0, 26))
        self.EL13.setFrameShape(QFrame.StyledPanel)
        self.EL13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.EL13)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.label_56 = QLabel(self.EL13)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setMaximumSize(QSize(110, 16777215))
        self.label_56.setFont(font6)
        self.label_56.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_38.addWidget(self.label_56)

        self.horizontalSpacer_79 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_79)

        self.E131 = QLineEdit(self.EL13)
        self.E131.setObjectName(u"E131")
        self.E131.setMinimumSize(QSize(50, 0))
        self.E131.setMaximumSize(QSize(50, 16777215))
        self.E131.setMouseTracking(False)
        self.E131.setStyleSheet(u"")
        self.E131.setAlignment(Qt.AlignCenter)
        self.E131.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_38.addWidget(self.E131)

        self.horizontalSpacer_80 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_80)

        self.E132 = QLineEdit(self.EL13)
        self.E132.setObjectName(u"E132")
        self.E132.setMinimumSize(QSize(50, 0))
        self.E132.setMaximumSize(QSize(50, 16777215))
        self.E132.setMouseTracking(False)
        self.E132.setStyleSheet(u"")
        self.E132.setAlignment(Qt.AlignCenter)
        self.E132.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_38.addWidget(self.E132)

        self.horizontalSpacer_81 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_81)


        self.verticalLayout_30.addWidget(self.EL13)

        self.EL14 = QFrame(self.frame_20)
        self.EL14.setObjectName(u"EL14")
        self.EL14.setMinimumSize(QSize(0, 26))
        self.EL14.setFrameShape(QFrame.StyledPanel)
        self.EL14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.EL14)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.label_59 = QLabel(self.EL14)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setMaximumSize(QSize(110, 16777215))
        self.label_59.setFont(font6)
        self.label_59.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_41.addWidget(self.label_59)

        self.horizontalSpacer_88 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_88)

        self.E141 = QLineEdit(self.EL14)
        self.E141.setObjectName(u"E141")
        self.E141.setMinimumSize(QSize(50, 0))
        self.E141.setMaximumSize(QSize(50, 16777215))
        self.E141.setMouseTracking(False)
        self.E141.setStyleSheet(u"")
        self.E141.setAlignment(Qt.AlignCenter)
        self.E141.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_41.addWidget(self.E141)

        self.horizontalSpacer_89 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_89)

        self.E142 = QLineEdit(self.EL14)
        self.E142.setObjectName(u"E142")
        self.E142.setMinimumSize(QSize(50, 0))
        self.E142.setMaximumSize(QSize(50, 16777215))
        self.E142.setMouseTracking(False)
        self.E142.setStyleSheet(u"")
        self.E142.setAlignment(Qt.AlignCenter)
        self.E142.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_41.addWidget(self.E142)

        self.horizontalSpacer_90 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_90)


        self.verticalLayout_30.addWidget(self.EL14)

        self.EL15 = QFrame(self.frame_20)
        self.EL15.setObjectName(u"EL15")
        self.EL15.setMinimumSize(QSize(0, 26))
        self.EL15.setFrameShape(QFrame.StyledPanel)
        self.EL15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.EL15)
        self.horizontalLayout_43.setSpacing(0)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.label_61 = QLabel(self.EL15)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setMaximumSize(QSize(110, 16777215))
        self.label_61.setFont(font6)
        self.label_61.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_43.addWidget(self.label_61)

        self.horizontalSpacer_94 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_43.addItem(self.horizontalSpacer_94)

        self.E151 = QLineEdit(self.EL15)
        self.E151.setObjectName(u"E151")
        self.E151.setMinimumSize(QSize(50, 0))
        self.E151.setMaximumSize(QSize(50, 16777215))
        self.E151.setMouseTracking(False)
        self.E151.setStyleSheet(u"")
        self.E151.setAlignment(Qt.AlignCenter)
        self.E151.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_43.addWidget(self.E151)

        self.horizontalSpacer_95 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_43.addItem(self.horizontalSpacer_95)

        self.E152 = QLineEdit(self.EL15)
        self.E152.setObjectName(u"E152")
        self.E152.setMinimumSize(QSize(50, 0))
        self.E152.setMaximumSize(QSize(50, 16777215))
        self.E152.setMouseTracking(False)
        self.E152.setStyleSheet(u"")
        self.E152.setAlignment(Qt.AlignCenter)
        self.E152.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_43.addWidget(self.E152)

        self.horizontalSpacer_96 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_43.addItem(self.horizontalSpacer_96)


        self.verticalLayout_30.addWidget(self.EL15)

        self.EL16 = QFrame(self.frame_20)
        self.EL16.setObjectName(u"EL16")
        self.EL16.setMinimumSize(QSize(0, 26))
        self.EL16.setFrameShape(QFrame.StyledPanel)
        self.EL16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.EL16)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.label_58 = QLabel(self.EL16)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setMaximumSize(QSize(110, 16777215))
        self.label_58.setFont(font6)
        self.label_58.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_40.addWidget(self.label_58)

        self.horizontalSpacer_85 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_40.addItem(self.horizontalSpacer_85)

        self.E161 = QLineEdit(self.EL16)
        self.E161.setObjectName(u"E161")
        self.E161.setMinimumSize(QSize(50, 0))
        self.E161.setMaximumSize(QSize(50, 16777215))
        self.E161.setMouseTracking(False)
        self.E161.setStyleSheet(u"")
        self.E161.setAlignment(Qt.AlignCenter)
        self.E161.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_40.addWidget(self.E161)

        self.horizontalSpacer_86 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_40.addItem(self.horizontalSpacer_86)

        self.E162 = QLineEdit(self.EL16)
        self.E162.setObjectName(u"E162")
        self.E162.setMinimumSize(QSize(50, 0))
        self.E162.setMaximumSize(QSize(50, 16777215))
        self.E162.setMouseTracking(False)
        self.E162.setStyleSheet(u"")
        self.E162.setAlignment(Qt.AlignCenter)
        self.E162.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_40.addWidget(self.E162)

        self.horizontalSpacer_87 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_40.addItem(self.horizontalSpacer_87)


        self.verticalLayout_30.addWidget(self.EL16)

        self.EL17 = QFrame(self.frame_20)
        self.EL17.setObjectName(u"EL17")
        self.EL17.setMinimumSize(QSize(0, 26))
        self.EL17.setFrameShape(QFrame.StyledPanel)
        self.EL17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.EL17)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.label_55 = QLabel(self.EL17)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setMaximumSize(QSize(110, 16777215))
        self.label_55.setFont(font6)
        self.label_55.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_37.addWidget(self.label_55)

        self.horizontalSpacer_76 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_76)

        self.E171 = QLineEdit(self.EL17)
        self.E171.setObjectName(u"E171")
        self.E171.setMinimumSize(QSize(50, 0))
        self.E171.setMaximumSize(QSize(50, 16777215))
        self.E171.setMouseTracking(False)
        self.E171.setStyleSheet(u"")
        self.E171.setAlignment(Qt.AlignCenter)
        self.E171.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_37.addWidget(self.E171)

        self.horizontalSpacer_77 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_77)

        self.E172 = QLineEdit(self.EL17)
        self.E172.setObjectName(u"E172")
        self.E172.setMinimumSize(QSize(50, 0))
        self.E172.setMaximumSize(QSize(50, 16777215))
        self.E172.setMouseTracking(False)
        self.E172.setStyleSheet(u"")
        self.E172.setAlignment(Qt.AlignCenter)
        self.E172.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_37.addWidget(self.E172)

        self.horizontalSpacer_78 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_78)


        self.verticalLayout_30.addWidget(self.EL17)

        self.EL18 = QFrame(self.frame_20)
        self.EL18.setObjectName(u"EL18")
        self.EL18.setMinimumSize(QSize(0, 26))
        self.EL18.setFrameShape(QFrame.StyledPanel)
        self.EL18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.EL18)
        self.horizontalLayout_56.setSpacing(0)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.label_74 = QLabel(self.EL18)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setMaximumSize(QSize(110, 16777215))
        self.label_74.setFont(font6)
        self.label_74.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_56.addWidget(self.label_74)

        self.horizontalSpacer_91 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_56.addItem(self.horizontalSpacer_91)

        self.E181 = QLineEdit(self.EL18)
        self.E181.setObjectName(u"E181")
        self.E181.setMinimumSize(QSize(50, 0))
        self.E181.setMaximumSize(QSize(50, 16777215))
        self.E181.setMouseTracking(False)
        self.E181.setStyleSheet(u"")
        self.E181.setAlignment(Qt.AlignCenter)
        self.E181.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_56.addWidget(self.E181)

        self.horizontalSpacer_92 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_56.addItem(self.horizontalSpacer_92)

        self.E182 = QLineEdit(self.EL18)
        self.E182.setObjectName(u"E182")
        self.E182.setMinimumSize(QSize(50, 0))
        self.E182.setMaximumSize(QSize(50, 16777215))
        self.E182.setMouseTracking(False)
        self.E182.setStyleSheet(u"")
        self.E182.setAlignment(Qt.AlignCenter)
        self.E182.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_56.addWidget(self.E182)

        self.horizontalSpacer_93 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_56.addItem(self.horizontalSpacer_93)


        self.verticalLayout_30.addWidget(self.EL18)

        self.EL19 = QFrame(self.frame_20)
        self.EL19.setObjectName(u"EL19")
        self.EL19.setMinimumSize(QSize(0, 26))
        self.EL19.setFrameShape(QFrame.StyledPanel)
        self.EL19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.EL19)
        self.horizontalLayout_57.setSpacing(0)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.label_75 = QLabel(self.EL19)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setMaximumSize(QSize(110, 16777215))
        self.label_75.setFont(font6)
        self.label_75.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_57.addWidget(self.label_75)

        self.horizontalSpacer_97 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_57.addItem(self.horizontalSpacer_97)

        self.E191 = QLineEdit(self.EL19)
        self.E191.setObjectName(u"E191")
        self.E191.setMinimumSize(QSize(50, 0))
        self.E191.setMaximumSize(QSize(50, 16777215))
        self.E191.setMouseTracking(False)
        self.E191.setStyleSheet(u"")
        self.E191.setAlignment(Qt.AlignCenter)
        self.E191.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_57.addWidget(self.E191)

        self.horizontalSpacer_98 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_57.addItem(self.horizontalSpacer_98)

        self.E192 = QLineEdit(self.EL19)
        self.E192.setObjectName(u"E192")
        self.E192.setMinimumSize(QSize(50, 0))
        self.E192.setMaximumSize(QSize(50, 16777215))
        self.E192.setMouseTracking(False)
        self.E192.setStyleSheet(u"")
        self.E192.setAlignment(Qt.AlignCenter)
        self.E192.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_57.addWidget(self.E192)

        self.horizontalSpacer_99 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_57.addItem(self.horizontalSpacer_99)


        self.verticalLayout_30.addWidget(self.EL19)

        self.EL20 = QFrame(self.frame_20)
        self.EL20.setObjectName(u"EL20")
        self.EL20.setMinimumSize(QSize(0, 26))
        self.EL20.setFrameShape(QFrame.StyledPanel)
        self.EL20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.EL20)
        self.horizontalLayout_58.setSpacing(0)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.label_76 = QLabel(self.EL20)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setMaximumSize(QSize(110, 16777215))
        self.label_76.setFont(font6)
        self.label_76.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_58.addWidget(self.label_76)

        self.horizontalSpacer_100 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_58.addItem(self.horizontalSpacer_100)

        self.E201 = QLineEdit(self.EL20)
        self.E201.setObjectName(u"E201")
        self.E201.setMinimumSize(QSize(50, 0))
        self.E201.setMaximumSize(QSize(50, 16777215))
        self.E201.setMouseTracking(False)
        self.E201.setStyleSheet(u"")
        self.E201.setAlignment(Qt.AlignCenter)
        self.E201.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_58.addWidget(self.E201)

        self.horizontalSpacer_101 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_58.addItem(self.horizontalSpacer_101)

        self.E202 = QLineEdit(self.EL20)
        self.E202.setObjectName(u"E202")
        self.E202.setMinimumSize(QSize(50, 0))
        self.E202.setMaximumSize(QSize(50, 16777215))
        self.E202.setMouseTracking(False)
        self.E202.setStyleSheet(u"")
        self.E202.setAlignment(Qt.AlignCenter)
        self.E202.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_58.addWidget(self.E202)

        self.horizontalSpacer_102 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_58.addItem(self.horizontalSpacer_102)


        self.verticalLayout_30.addWidget(self.EL20)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_30.addItem(self.verticalSpacer_5)


        self.horizontalLayout_10.addWidget(self.frame_20)

        self.frame_19 = QFrame(self.frame_18)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_19)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_name_2 = QFrame(self.frame_19)
        self.frame_name_2.setObjectName(u"frame_name_2")
        self.frame_name_2.setMinimumSize(QSize(0, 40))
        self.frame_name_2.setMaximumSize(QSize(16777215, 40))
        self.frame_name_2.setFrameShape(QFrame.StyledPanel)
        self.frame_name_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_name_2)
        self.verticalLayout_31.setSpacing(3)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 10)
        self.frame_126 = QFrame(self.frame_name_2)
        self.frame_126.setObjectName(u"frame_126")
        self.frame_126.setFrameShape(QFrame.StyledPanel)
        self.frame_126.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_126)
        self.horizontalLayout_19.setSpacing(50)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(25, 0, 32, 0)
        self.label_29 = QLabel(self.frame_126)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMaximumSize(QSize(90, 16777215))
        self.label_29.setFont(font5)
        self.label_29.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.label_29)

        self.label_32 = QLabel(self.frame_126)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMaximumSize(QSize(100, 16777215))
        self.label_32.setFont(font5)
        self.label_32.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.label_32)

        self.label_139 = QLabel(self.frame_126)
        self.label_139.setObjectName(u"label_139")
        self.label_139.setMaximumSize(QSize(100, 16777215))
        self.label_139.setFont(font5)
        self.label_139.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.label_139)


        self.verticalLayout_31.addWidget(self.frame_126)

        self.line_8 = QFrame(self.frame_name_2)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setMinimumSize(QSize(0, 2))
        self.line_8.setMaximumSize(QSize(16777215, 2))
        self.line_8.setStyleSheet(u"border: 1px solid rgb(0, 0, 0);")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_31.addWidget(self.line_8)


        self.verticalLayout_12.addWidget(self.frame_name_2)

        self.EL21 = QFrame(self.frame_19)
        self.EL21.setObjectName(u"EL21")
        self.EL21.setMinimumSize(QSize(0, 26))
        self.EL21.setMaximumSize(QSize(16777215, 26))
        self.EL21.setFrameShape(QFrame.StyledPanel)
        self.EL21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_137 = QHBoxLayout(self.EL21)
        self.horizontalLayout_137.setSpacing(0)
        self.horizontalLayout_137.setObjectName(u"horizontalLayout_137")
        self.horizontalLayout_137.setContentsMargins(0, 0, 0, 0)
        self.label_161 = QLabel(self.EL21)
        self.label_161.setObjectName(u"label_161")
        self.label_161.setMaximumSize(QSize(110, 16777215))
        self.label_161.setFont(font6)
        self.label_161.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_137.addWidget(self.label_161)

        self.horizontalSpacer_316 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_137.addItem(self.horizontalSpacer_316)

        self.E211 = QLineEdit(self.EL21)
        self.E211.setObjectName(u"E211")
        self.E211.setMinimumSize(QSize(50, 0))
        self.E211.setMaximumSize(QSize(50, 16777215))
        self.E211.setMouseTracking(False)
        self.E211.setStyleSheet(u"")
        self.E211.setAlignment(Qt.AlignCenter)
        self.E211.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_137.addWidget(self.E211)

        self.horizontalSpacer_317 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_137.addItem(self.horizontalSpacer_317)

        self.E212 = QLineEdit(self.EL21)
        self.E212.setObjectName(u"E212")
        self.E212.setMinimumSize(QSize(50, 0))
        self.E212.setMaximumSize(QSize(50, 16777215))
        self.E212.setMouseTracking(False)
        self.E212.setStyleSheet(u"")
        self.E212.setAlignment(Qt.AlignCenter)
        self.E212.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_137.addWidget(self.E212)

        self.horizontalSpacer_318 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_137.addItem(self.horizontalSpacer_318)


        self.verticalLayout_12.addWidget(self.EL21)

        self.EL22 = QFrame(self.frame_19)
        self.EL22.setObjectName(u"EL22")
        self.EL22.setMinimumSize(QSize(0, 26))
        self.EL22.setMaximumSize(QSize(16777215, 26))
        self.EL22.setFrameShape(QFrame.StyledPanel)
        self.EL22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_139 = QHBoxLayout(self.EL22)
        self.horizontalLayout_139.setSpacing(0)
        self.horizontalLayout_139.setObjectName(u"horizontalLayout_139")
        self.horizontalLayout_139.setContentsMargins(0, 0, 0, 0)
        self.label_163 = QLabel(self.EL22)
        self.label_163.setObjectName(u"label_163")
        self.label_163.setMaximumSize(QSize(110, 16777215))
        self.label_163.setFont(font6)
        self.label_163.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_139.addWidget(self.label_163)

        self.horizontalSpacer_322 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_139.addItem(self.horizontalSpacer_322)

        self.E221 = QLineEdit(self.EL22)
        self.E221.setObjectName(u"E221")
        self.E221.setMinimumSize(QSize(50, 0))
        self.E221.setMaximumSize(QSize(50, 16777215))
        self.E221.setMouseTracking(False)
        self.E221.setStyleSheet(u"")
        self.E221.setAlignment(Qt.AlignCenter)
        self.E221.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_139.addWidget(self.E221)

        self.horizontalSpacer_323 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_139.addItem(self.horizontalSpacer_323)

        self.E222 = QLineEdit(self.EL22)
        self.E222.setObjectName(u"E222")
        self.E222.setMinimumSize(QSize(50, 0))
        self.E222.setMaximumSize(QSize(50, 16777215))
        self.E222.setMouseTracking(False)
        self.E222.setStyleSheet(u"")
        self.E222.setAlignment(Qt.AlignCenter)
        self.E222.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_139.addWidget(self.E222)

        self.horizontalSpacer_324 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_139.addItem(self.horizontalSpacer_324)


        self.verticalLayout_12.addWidget(self.EL22)

        self.EL23 = QFrame(self.frame_19)
        self.EL23.setObjectName(u"EL23")
        self.EL23.setMinimumSize(QSize(0, 26))
        self.EL23.setMaximumSize(QSize(16777215, 26))
        self.EL23.setFrameShape(QFrame.StyledPanel)
        self.EL23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_151 = QHBoxLayout(self.EL23)
        self.horizontalLayout_151.setSpacing(0)
        self.horizontalLayout_151.setObjectName(u"horizontalLayout_151")
        self.horizontalLayout_151.setContentsMargins(0, 0, 0, 0)
        self.label_175 = QLabel(self.EL23)
        self.label_175.setObjectName(u"label_175")
        self.label_175.setMaximumSize(QSize(110, 16777215))
        self.label_175.setFont(font6)
        self.label_175.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_151.addWidget(self.label_175)

        self.horizontalSpacer_358 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_151.addItem(self.horizontalSpacer_358)

        self.E231 = QLineEdit(self.EL23)
        self.E231.setObjectName(u"E231")
        self.E231.setMinimumSize(QSize(50, 0))
        self.E231.setMaximumSize(QSize(50, 16777215))
        self.E231.setMouseTracking(False)
        self.E231.setStyleSheet(u"")
        self.E231.setAlignment(Qt.AlignCenter)
        self.E231.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_151.addWidget(self.E231)

        self.horizontalSpacer_359 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_151.addItem(self.horizontalSpacer_359)

        self.E232 = QLineEdit(self.EL23)
        self.E232.setObjectName(u"E232")
        self.E232.setMinimumSize(QSize(50, 0))
        self.E232.setMaximumSize(QSize(50, 16777215))
        self.E232.setMouseTracking(False)
        self.E232.setStyleSheet(u"")
        self.E232.setAlignment(Qt.AlignCenter)
        self.E232.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_151.addWidget(self.E232)

        self.horizontalSpacer_360 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_151.addItem(self.horizontalSpacer_360)


        self.verticalLayout_12.addWidget(self.EL23)

        self.EL24 = QFrame(self.frame_19)
        self.EL24.setObjectName(u"EL24")
        self.EL24.setMinimumSize(QSize(0, 26))
        self.EL24.setMaximumSize(QSize(16777215, 26))
        self.EL24.setFrameShape(QFrame.StyledPanel)
        self.EL24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_142 = QHBoxLayout(self.EL24)
        self.horizontalLayout_142.setSpacing(0)
        self.horizontalLayout_142.setObjectName(u"horizontalLayout_142")
        self.horizontalLayout_142.setContentsMargins(0, 0, 0, 0)
        self.label_166 = QLabel(self.EL24)
        self.label_166.setObjectName(u"label_166")
        self.label_166.setMaximumSize(QSize(110, 16777215))
        self.label_166.setFont(font6)
        self.label_166.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_142.addWidget(self.label_166)

        self.horizontalSpacer_331 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_142.addItem(self.horizontalSpacer_331)

        self.E241 = QLineEdit(self.EL24)
        self.E241.setObjectName(u"E241")
        self.E241.setMinimumSize(QSize(50, 0))
        self.E241.setMaximumSize(QSize(50, 16777215))
        self.E241.setMouseTracking(False)
        self.E241.setStyleSheet(u"")
        self.E241.setAlignment(Qt.AlignCenter)
        self.E241.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_142.addWidget(self.E241)

        self.horizontalSpacer_332 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_142.addItem(self.horizontalSpacer_332)

        self.E242 = QLineEdit(self.EL24)
        self.E242.setObjectName(u"E242")
        self.E242.setMinimumSize(QSize(50, 0))
        self.E242.setMaximumSize(QSize(50, 16777215))
        self.E242.setMouseTracking(False)
        self.E242.setStyleSheet(u"")
        self.E242.setAlignment(Qt.AlignCenter)
        self.E242.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_142.addWidget(self.E242)

        self.horizontalSpacer_333 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_142.addItem(self.horizontalSpacer_333)


        self.verticalLayout_12.addWidget(self.EL24)

        self.EL25 = QFrame(self.frame_19)
        self.EL25.setObjectName(u"EL25")
        self.EL25.setMinimumSize(QSize(0, 26))
        self.EL25.setMaximumSize(QSize(16777215, 26))
        self.EL25.setFrameShape(QFrame.StyledPanel)
        self.EL25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_147 = QHBoxLayout(self.EL25)
        self.horizontalLayout_147.setSpacing(0)
        self.horizontalLayout_147.setObjectName(u"horizontalLayout_147")
        self.horizontalLayout_147.setContentsMargins(0, 0, 0, 0)
        self.label_171 = QLabel(self.EL25)
        self.label_171.setObjectName(u"label_171")
        self.label_171.setMaximumSize(QSize(110, 16777215))
        self.label_171.setFont(font6)
        self.label_171.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_147.addWidget(self.label_171)

        self.horizontalSpacer_346 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_147.addItem(self.horizontalSpacer_346)

        self.E251 = QLineEdit(self.EL25)
        self.E251.setObjectName(u"E251")
        self.E251.setMinimumSize(QSize(50, 0))
        self.E251.setMaximumSize(QSize(50, 16777215))
        self.E251.setMouseTracking(False)
        self.E251.setStyleSheet(u"")
        self.E251.setAlignment(Qt.AlignCenter)
        self.E251.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_147.addWidget(self.E251)

        self.horizontalSpacer_347 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_147.addItem(self.horizontalSpacer_347)

        self.E252 = QLineEdit(self.EL25)
        self.E252.setObjectName(u"E252")
        self.E252.setMinimumSize(QSize(50, 0))
        self.E252.setMaximumSize(QSize(50, 16777215))
        self.E252.setMouseTracking(False)
        self.E252.setStyleSheet(u"")
        self.E252.setAlignment(Qt.AlignCenter)
        self.E252.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_147.addWidget(self.E252)

        self.horizontalSpacer_348 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_147.addItem(self.horizontalSpacer_348)


        self.verticalLayout_12.addWidget(self.EL25)

        self.EL26 = QFrame(self.frame_19)
        self.EL26.setObjectName(u"EL26")
        self.EL26.setMinimumSize(QSize(0, 26))
        self.EL26.setMaximumSize(QSize(16777215, 26))
        self.EL26.setFrameShape(QFrame.StyledPanel)
        self.EL26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_153 = QHBoxLayout(self.EL26)
        self.horizontalLayout_153.setSpacing(0)
        self.horizontalLayout_153.setObjectName(u"horizontalLayout_153")
        self.horizontalLayout_153.setContentsMargins(0, 0, 0, 0)
        self.label_177 = QLabel(self.EL26)
        self.label_177.setObjectName(u"label_177")
        self.label_177.setMaximumSize(QSize(110, 16777215))
        self.label_177.setFont(font6)
        self.label_177.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_153.addWidget(self.label_177)

        self.horizontalSpacer_364 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_153.addItem(self.horizontalSpacer_364)

        self.E261 = QLineEdit(self.EL26)
        self.E261.setObjectName(u"E261")
        self.E261.setMinimumSize(QSize(50, 0))
        self.E261.setMaximumSize(QSize(50, 16777215))
        self.E261.setMouseTracking(False)
        self.E261.setStyleSheet(u"")
        self.E261.setAlignment(Qt.AlignCenter)
        self.E261.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_153.addWidget(self.E261)

        self.horizontalSpacer_365 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_153.addItem(self.horizontalSpacer_365)

        self.E262 = QLineEdit(self.EL26)
        self.E262.setObjectName(u"E262")
        self.E262.setMinimumSize(QSize(50, 0))
        self.E262.setMaximumSize(QSize(50, 16777215))
        self.E262.setMouseTracking(False)
        self.E262.setStyleSheet(u"")
        self.E262.setAlignment(Qt.AlignCenter)
        self.E262.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_153.addWidget(self.E262)

        self.horizontalSpacer_366 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_153.addItem(self.horizontalSpacer_366)


        self.verticalLayout_12.addWidget(self.EL26)

        self.EL27 = QFrame(self.frame_19)
        self.EL27.setObjectName(u"EL27")
        self.EL27.setMinimumSize(QSize(0, 26))
        self.EL27.setMaximumSize(QSize(16777215, 26))
        self.EL27.setFrameShape(QFrame.StyledPanel)
        self.EL27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_135 = QHBoxLayout(self.EL27)
        self.horizontalLayout_135.setSpacing(0)
        self.horizontalLayout_135.setObjectName(u"horizontalLayout_135")
        self.horizontalLayout_135.setContentsMargins(0, 0, 0, 0)
        self.label_159 = QLabel(self.EL27)
        self.label_159.setObjectName(u"label_159")
        self.label_159.setMaximumSize(QSize(110, 16777215))
        self.label_159.setFont(font6)
        self.label_159.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_135.addWidget(self.label_159)

        self.horizontalSpacer_310 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_135.addItem(self.horizontalSpacer_310)

        self.E271 = QLineEdit(self.EL27)
        self.E271.setObjectName(u"E271")
        self.E271.setMinimumSize(QSize(50, 0))
        self.E271.setMaximumSize(QSize(50, 16777215))
        self.E271.setMouseTracking(False)
        self.E271.setStyleSheet(u"")
        self.E271.setAlignment(Qt.AlignCenter)
        self.E271.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_135.addWidget(self.E271)

        self.horizontalSpacer_311 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_135.addItem(self.horizontalSpacer_311)

        self.E272 = QLineEdit(self.EL27)
        self.E272.setObjectName(u"E272")
        self.E272.setMinimumSize(QSize(50, 0))
        self.E272.setMaximumSize(QSize(50, 16777215))
        self.E272.setMouseTracking(False)
        self.E272.setStyleSheet(u"")
        self.E272.setAlignment(Qt.AlignCenter)
        self.E272.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_135.addWidget(self.E272)

        self.horizontalSpacer_312 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_135.addItem(self.horizontalSpacer_312)


        self.verticalLayout_12.addWidget(self.EL27)

        self.EL28 = QFrame(self.frame_19)
        self.EL28.setObjectName(u"EL28")
        self.EL28.setMinimumSize(QSize(0, 26))
        self.EL28.setMaximumSize(QSize(16777215, 26))
        self.EL28.setFrameShape(QFrame.StyledPanel)
        self.EL28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_143 = QHBoxLayout(self.EL28)
        self.horizontalLayout_143.setSpacing(0)
        self.horizontalLayout_143.setObjectName(u"horizontalLayout_143")
        self.horizontalLayout_143.setContentsMargins(0, 0, 0, 0)
        self.label_167 = QLabel(self.EL28)
        self.label_167.setObjectName(u"label_167")
        self.label_167.setMaximumSize(QSize(110, 16777215))
        self.label_167.setFont(font6)
        self.label_167.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_143.addWidget(self.label_167)

        self.horizontalSpacer_334 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_143.addItem(self.horizontalSpacer_334)

        self.E281 = QLineEdit(self.EL28)
        self.E281.setObjectName(u"E281")
        self.E281.setMinimumSize(QSize(50, 0))
        self.E281.setMaximumSize(QSize(50, 16777215))
        self.E281.setMouseTracking(False)
        self.E281.setStyleSheet(u"")
        self.E281.setAlignment(Qt.AlignCenter)
        self.E281.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_143.addWidget(self.E281)

        self.horizontalSpacer_335 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_143.addItem(self.horizontalSpacer_335)

        self.E282 = QLineEdit(self.EL28)
        self.E282.setObjectName(u"E282")
        self.E282.setMinimumSize(QSize(50, 0))
        self.E282.setMaximumSize(QSize(50, 16777215))
        self.E282.setMouseTracking(False)
        self.E282.setStyleSheet(u"")
        self.E282.setAlignment(Qt.AlignCenter)
        self.E282.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_143.addWidget(self.E282)

        self.horizontalSpacer_336 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_143.addItem(self.horizontalSpacer_336)


        self.verticalLayout_12.addWidget(self.EL28)

        self.EL29 = QFrame(self.frame_19)
        self.EL29.setObjectName(u"EL29")
        self.EL29.setMinimumSize(QSize(0, 26))
        self.EL29.setMaximumSize(QSize(16777215, 26))
        self.EL29.setFrameShape(QFrame.StyledPanel)
        self.EL29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_144 = QHBoxLayout(self.EL29)
        self.horizontalLayout_144.setSpacing(0)
        self.horizontalLayout_144.setObjectName(u"horizontalLayout_144")
        self.horizontalLayout_144.setContentsMargins(0, 0, 0, 0)
        self.label_168 = QLabel(self.EL29)
        self.label_168.setObjectName(u"label_168")
        self.label_168.setMaximumSize(QSize(110, 16777215))
        self.label_168.setFont(font6)
        self.label_168.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_144.addWidget(self.label_168)

        self.horizontalSpacer_337 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_144.addItem(self.horizontalSpacer_337)

        self.E291 = QLineEdit(self.EL29)
        self.E291.setObjectName(u"E291")
        self.E291.setMinimumSize(QSize(50, 0))
        self.E291.setMaximumSize(QSize(50, 16777215))
        self.E291.setMouseTracking(False)
        self.E291.setStyleSheet(u"")
        self.E291.setAlignment(Qt.AlignCenter)
        self.E291.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_144.addWidget(self.E291)

        self.horizontalSpacer_338 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_144.addItem(self.horizontalSpacer_338)

        self.E292 = QLineEdit(self.EL29)
        self.E292.setObjectName(u"E292")
        self.E292.setMinimumSize(QSize(50, 0))
        self.E292.setMaximumSize(QSize(50, 16777215))
        self.E292.setMouseTracking(False)
        self.E292.setStyleSheet(u"")
        self.E292.setAlignment(Qt.AlignCenter)
        self.E292.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_144.addWidget(self.E292)

        self.horizontalSpacer_339 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_144.addItem(self.horizontalSpacer_339)


        self.verticalLayout_12.addWidget(self.EL29)

        self.EL30 = QFrame(self.frame_19)
        self.EL30.setObjectName(u"EL30")
        self.EL30.setMinimumSize(QSize(0, 26))
        self.EL30.setMaximumSize(QSize(16777215, 26))
        self.EL30.setFrameShape(QFrame.StyledPanel)
        self.EL30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_152 = QHBoxLayout(self.EL30)
        self.horizontalLayout_152.setSpacing(0)
        self.horizontalLayout_152.setObjectName(u"horizontalLayout_152")
        self.horizontalLayout_152.setContentsMargins(0, 0, 0, 0)
        self.label_176 = QLabel(self.EL30)
        self.label_176.setObjectName(u"label_176")
        self.label_176.setMaximumSize(QSize(110, 16777215))
        self.label_176.setFont(font6)
        self.label_176.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_152.addWidget(self.label_176)

        self.horizontalSpacer_361 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_152.addItem(self.horizontalSpacer_361)

        self.E301 = QLineEdit(self.EL30)
        self.E301.setObjectName(u"E301")
        self.E301.setMinimumSize(QSize(50, 0))
        self.E301.setMaximumSize(QSize(50, 16777215))
        self.E301.setMouseTracking(False)
        self.E301.setStyleSheet(u"")
        self.E301.setAlignment(Qt.AlignCenter)
        self.E301.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_152.addWidget(self.E301)

        self.horizontalSpacer_362 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_152.addItem(self.horizontalSpacer_362)

        self.E302 = QLineEdit(self.EL30)
        self.E302.setObjectName(u"E302")
        self.E302.setMinimumSize(QSize(50, 0))
        self.E302.setMaximumSize(QSize(50, 16777215))
        self.E302.setMouseTracking(False)
        self.E302.setStyleSheet(u"")
        self.E302.setAlignment(Qt.AlignCenter)
        self.E302.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_152.addWidget(self.E302)

        self.horizontalSpacer_363 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_152.addItem(self.horizontalSpacer_363)


        self.verticalLayout_12.addWidget(self.EL30)

        self.EL31 = QFrame(self.frame_19)
        self.EL31.setObjectName(u"EL31")
        self.EL31.setMinimumSize(QSize(0, 26))
        self.EL31.setMaximumSize(QSize(16777215, 26))
        self.EL31.setFrameShape(QFrame.StyledPanel)
        self.EL31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_149 = QHBoxLayout(self.EL31)
        self.horizontalLayout_149.setSpacing(0)
        self.horizontalLayout_149.setObjectName(u"horizontalLayout_149")
        self.horizontalLayout_149.setContentsMargins(0, 0, 0, 0)
        self.label_173 = QLabel(self.EL31)
        self.label_173.setObjectName(u"label_173")
        self.label_173.setMaximumSize(QSize(110, 16777215))
        self.label_173.setFont(font6)
        self.label_173.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_149.addWidget(self.label_173)

        self.horizontalSpacer_352 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_149.addItem(self.horizontalSpacer_352)

        self.E311 = QLineEdit(self.EL31)
        self.E311.setObjectName(u"E311")
        self.E311.setMinimumSize(QSize(50, 0))
        self.E311.setMaximumSize(QSize(50, 16777215))
        self.E311.setMouseTracking(False)
        self.E311.setStyleSheet(u"")
        self.E311.setAlignment(Qt.AlignCenter)
        self.E311.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_149.addWidget(self.E311)

        self.horizontalSpacer_353 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_149.addItem(self.horizontalSpacer_353)

        self.E312 = QLineEdit(self.EL31)
        self.E312.setObjectName(u"E312")
        self.E312.setMinimumSize(QSize(50, 0))
        self.E312.setMaximumSize(QSize(50, 16777215))
        self.E312.setMouseTracking(False)
        self.E312.setStyleSheet(u"")
        self.E312.setAlignment(Qt.AlignCenter)
        self.E312.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_149.addWidget(self.E312)

        self.horizontalSpacer_354 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_149.addItem(self.horizontalSpacer_354)


        self.verticalLayout_12.addWidget(self.EL31)

        self.EL32 = QFrame(self.frame_19)
        self.EL32.setObjectName(u"EL32")
        self.EL32.setMinimumSize(QSize(0, 26))
        self.EL32.setMaximumSize(QSize(16777215, 26))
        self.EL32.setFrameShape(QFrame.StyledPanel)
        self.EL32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_154 = QHBoxLayout(self.EL32)
        self.horizontalLayout_154.setSpacing(0)
        self.horizontalLayout_154.setObjectName(u"horizontalLayout_154")
        self.horizontalLayout_154.setContentsMargins(0, 0, 0, 0)
        self.label_178 = QLabel(self.EL32)
        self.label_178.setObjectName(u"label_178")
        self.label_178.setMaximumSize(QSize(110, 16777215))
        self.label_178.setFont(font6)
        self.label_178.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_154.addWidget(self.label_178)

        self.horizontalSpacer_367 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_154.addItem(self.horizontalSpacer_367)

        self.E321 = QLineEdit(self.EL32)
        self.E321.setObjectName(u"E321")
        self.E321.setMinimumSize(QSize(50, 0))
        self.E321.setMaximumSize(QSize(50, 16777215))
        self.E321.setMouseTracking(False)
        self.E321.setStyleSheet(u"")
        self.E321.setAlignment(Qt.AlignCenter)
        self.E321.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_154.addWidget(self.E321)

        self.horizontalSpacer_368 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_154.addItem(self.horizontalSpacer_368)

        self.E322 = QLineEdit(self.EL32)
        self.E322.setObjectName(u"E322")
        self.E322.setMinimumSize(QSize(50, 0))
        self.E322.setMaximumSize(QSize(50, 16777215))
        self.E322.setMouseTracking(False)
        self.E322.setStyleSheet(u"")
        self.E322.setAlignment(Qt.AlignCenter)
        self.E322.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_154.addWidget(self.E322)

        self.horizontalSpacer_369 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_154.addItem(self.horizontalSpacer_369)


        self.verticalLayout_12.addWidget(self.EL32)

        self.EL33 = QFrame(self.frame_19)
        self.EL33.setObjectName(u"EL33")
        self.EL33.setMinimumSize(QSize(0, 26))
        self.EL33.setMaximumSize(QSize(16777215, 26))
        self.EL33.setFrameShape(QFrame.StyledPanel)
        self.EL33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_136 = QHBoxLayout(self.EL33)
        self.horizontalLayout_136.setSpacing(0)
        self.horizontalLayout_136.setObjectName(u"horizontalLayout_136")
        self.horizontalLayout_136.setContentsMargins(0, 0, 0, 0)
        self.label_160 = QLabel(self.EL33)
        self.label_160.setObjectName(u"label_160")
        self.label_160.setMaximumSize(QSize(110, 16777215))
        self.label_160.setFont(font6)
        self.label_160.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_136.addWidget(self.label_160)

        self.horizontalSpacer_313 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_136.addItem(self.horizontalSpacer_313)

        self.E331 = QLineEdit(self.EL33)
        self.E331.setObjectName(u"E331")
        self.E331.setMinimumSize(QSize(50, 0))
        self.E331.setMaximumSize(QSize(50, 16777215))
        self.E331.setMouseTracking(False)
        self.E331.setStyleSheet(u"")
        self.E331.setAlignment(Qt.AlignCenter)
        self.E331.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_136.addWidget(self.E331)

        self.horizontalSpacer_314 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_136.addItem(self.horizontalSpacer_314)

        self.E332 = QLineEdit(self.EL33)
        self.E332.setObjectName(u"E332")
        self.E332.setMinimumSize(QSize(50, 0))
        self.E332.setMaximumSize(QSize(50, 16777215))
        self.E332.setMouseTracking(False)
        self.E332.setStyleSheet(u"")
        self.E332.setAlignment(Qt.AlignCenter)
        self.E332.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_136.addWidget(self.E332)

        self.horizontalSpacer_315 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_136.addItem(self.horizontalSpacer_315)


        self.verticalLayout_12.addWidget(self.EL33)

        self.EL34 = QFrame(self.frame_19)
        self.EL34.setObjectName(u"EL34")
        self.EL34.setMinimumSize(QSize(0, 26))
        self.EL34.setMaximumSize(QSize(16777215, 26))
        self.EL34.setFrameShape(QFrame.StyledPanel)
        self.EL34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_145 = QHBoxLayout(self.EL34)
        self.horizontalLayout_145.setSpacing(0)
        self.horizontalLayout_145.setObjectName(u"horizontalLayout_145")
        self.horizontalLayout_145.setContentsMargins(0, 0, 0, 0)
        self.label_169 = QLabel(self.EL34)
        self.label_169.setObjectName(u"label_169")
        self.label_169.setMaximumSize(QSize(110, 16777215))
        self.label_169.setFont(font6)
        self.label_169.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_145.addWidget(self.label_169)

        self.horizontalSpacer_340 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_145.addItem(self.horizontalSpacer_340)

        self.E341 = QLineEdit(self.EL34)
        self.E341.setObjectName(u"E341")
        self.E341.setMinimumSize(QSize(50, 0))
        self.E341.setMaximumSize(QSize(50, 16777215))
        self.E341.setMouseTracking(False)
        self.E341.setStyleSheet(u"")
        self.E341.setAlignment(Qt.AlignCenter)
        self.E341.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_145.addWidget(self.E341)

        self.horizontalSpacer_341 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_145.addItem(self.horizontalSpacer_341)

        self.E342 = QLineEdit(self.EL34)
        self.E342.setObjectName(u"E342")
        self.E342.setMinimumSize(QSize(50, 0))
        self.E342.setMaximumSize(QSize(50, 16777215))
        self.E342.setMouseTracking(False)
        self.E342.setStyleSheet(u"")
        self.E342.setAlignment(Qt.AlignCenter)
        self.E342.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_145.addWidget(self.E342)

        self.horizontalSpacer_342 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_145.addItem(self.horizontalSpacer_342)


        self.verticalLayout_12.addWidget(self.EL34)

        self.EL35 = QFrame(self.frame_19)
        self.EL35.setObjectName(u"EL35")
        self.EL35.setMinimumSize(QSize(0, 26))
        self.EL35.setMaximumSize(QSize(16777215, 26))
        self.EL35.setFrameShape(QFrame.StyledPanel)
        self.EL35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_150 = QHBoxLayout(self.EL35)
        self.horizontalLayout_150.setSpacing(0)
        self.horizontalLayout_150.setObjectName(u"horizontalLayout_150")
        self.horizontalLayout_150.setContentsMargins(0, 0, 0, 0)
        self.label_174 = QLabel(self.EL35)
        self.label_174.setObjectName(u"label_174")
        self.label_174.setMaximumSize(QSize(110, 16777215))
        self.label_174.setFont(font6)
        self.label_174.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_150.addWidget(self.label_174)

        self.horizontalSpacer_355 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_150.addItem(self.horizontalSpacer_355)

        self.E351 = QLineEdit(self.EL35)
        self.E351.setObjectName(u"E351")
        self.E351.setMinimumSize(QSize(50, 0))
        self.E351.setMaximumSize(QSize(50, 16777215))
        self.E351.setMouseTracking(False)
        self.E351.setStyleSheet(u"")
        self.E351.setAlignment(Qt.AlignCenter)
        self.E351.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_150.addWidget(self.E351)

        self.horizontalSpacer_356 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_150.addItem(self.horizontalSpacer_356)

        self.E352 = QLineEdit(self.EL35)
        self.E352.setObjectName(u"E352")
        self.E352.setMinimumSize(QSize(50, 0))
        self.E352.setMaximumSize(QSize(50, 16777215))
        self.E352.setMouseTracking(False)
        self.E352.setStyleSheet(u"")
        self.E352.setAlignment(Qt.AlignCenter)
        self.E352.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_150.addWidget(self.E352)

        self.horizontalSpacer_357 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_150.addItem(self.horizontalSpacer_357)


        self.verticalLayout_12.addWidget(self.EL35)

        self.EL36 = QFrame(self.frame_19)
        self.EL36.setObjectName(u"EL36")
        self.EL36.setMinimumSize(QSize(0, 26))
        self.EL36.setMaximumSize(QSize(16777215, 26))
        self.EL36.setFrameShape(QFrame.StyledPanel)
        self.EL36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_138 = QHBoxLayout(self.EL36)
        self.horizontalLayout_138.setSpacing(0)
        self.horizontalLayout_138.setObjectName(u"horizontalLayout_138")
        self.horizontalLayout_138.setContentsMargins(0, 0, 0, 0)
        self.label_162 = QLabel(self.EL36)
        self.label_162.setObjectName(u"label_162")
        self.label_162.setMaximumSize(QSize(110, 16777215))
        self.label_162.setFont(font6)
        self.label_162.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_138.addWidget(self.label_162)

        self.horizontalSpacer_319 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_138.addItem(self.horizontalSpacer_319)

        self.E361 = QLineEdit(self.EL36)
        self.E361.setObjectName(u"E361")
        self.E361.setMinimumSize(QSize(50, 0))
        self.E361.setMaximumSize(QSize(50, 16777215))
        self.E361.setMouseTracking(False)
        self.E361.setStyleSheet(u"")
        self.E361.setAlignment(Qt.AlignCenter)
        self.E361.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_138.addWidget(self.E361)

        self.horizontalSpacer_320 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_138.addItem(self.horizontalSpacer_320)

        self.E362 = QLineEdit(self.EL36)
        self.E362.setObjectName(u"E362")
        self.E362.setMinimumSize(QSize(50, 0))
        self.E362.setMaximumSize(QSize(50, 16777215))
        self.E362.setMouseTracking(False)
        self.E362.setStyleSheet(u"")
        self.E362.setAlignment(Qt.AlignCenter)
        self.E362.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_138.addWidget(self.E362)

        self.horizontalSpacer_321 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_138.addItem(self.horizontalSpacer_321)


        self.verticalLayout_12.addWidget(self.EL36)

        self.EL37 = QFrame(self.frame_19)
        self.EL37.setObjectName(u"EL37")
        self.EL37.setMinimumSize(QSize(0, 26))
        self.EL37.setMaximumSize(QSize(16777215, 26))
        self.EL37.setFrameShape(QFrame.StyledPanel)
        self.EL37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_148 = QHBoxLayout(self.EL37)
        self.horizontalLayout_148.setSpacing(0)
        self.horizontalLayout_148.setObjectName(u"horizontalLayout_148")
        self.horizontalLayout_148.setContentsMargins(0, 0, 0, 0)
        self.label_172 = QLabel(self.EL37)
        self.label_172.setObjectName(u"label_172")
        self.label_172.setMaximumSize(QSize(110, 16777215))
        self.label_172.setFont(font6)
        self.label_172.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_148.addWidget(self.label_172)

        self.horizontalSpacer_349 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_148.addItem(self.horizontalSpacer_349)

        self.E371 = QLineEdit(self.EL37)
        self.E371.setObjectName(u"E371")
        self.E371.setMinimumSize(QSize(50, 0))
        self.E371.setMaximumSize(QSize(50, 16777215))
        self.E371.setMouseTracking(False)
        self.E371.setStyleSheet(u"")
        self.E371.setAlignment(Qt.AlignCenter)
        self.E371.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_148.addWidget(self.E371)

        self.horizontalSpacer_350 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_148.addItem(self.horizontalSpacer_350)

        self.E372 = QLineEdit(self.EL37)
        self.E372.setObjectName(u"E372")
        self.E372.setMinimumSize(QSize(50, 0))
        self.E372.setMaximumSize(QSize(50, 16777215))
        self.E372.setMouseTracking(False)
        self.E372.setStyleSheet(u"")
        self.E372.setAlignment(Qt.AlignCenter)
        self.E372.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_148.addWidget(self.E372)

        self.horizontalSpacer_351 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_148.addItem(self.horizontalSpacer_351)


        self.verticalLayout_12.addWidget(self.EL37)

        self.EL38 = QFrame(self.frame_19)
        self.EL38.setObjectName(u"EL38")
        self.EL38.setMinimumSize(QSize(0, 26))
        self.EL38.setMaximumSize(QSize(16777215, 26))
        self.EL38.setFrameShape(QFrame.StyledPanel)
        self.EL38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_60 = QHBoxLayout(self.EL38)
        self.horizontalLayout_60.setSpacing(0)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.label_78 = QLabel(self.EL38)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setMaximumSize(QSize(110, 16777215))
        self.label_78.setFont(font6)
        self.label_78.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_60.addWidget(self.label_78)

        self.horizontalSpacer_106 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_60.addItem(self.horizontalSpacer_106)

        self.E381 = QLineEdit(self.EL38)
        self.E381.setObjectName(u"E381")
        self.E381.setMinimumSize(QSize(50, 0))
        self.E381.setMaximumSize(QSize(50, 16777215))
        self.E381.setMouseTracking(False)
        self.E381.setStyleSheet(u"")
        self.E381.setAlignment(Qt.AlignCenter)
        self.E381.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_60.addWidget(self.E381)

        self.horizontalSpacer_107 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_60.addItem(self.horizontalSpacer_107)

        self.E382 = QLineEdit(self.EL38)
        self.E382.setObjectName(u"E382")
        self.E382.setMinimumSize(QSize(50, 0))
        self.E382.setMaximumSize(QSize(50, 16777215))
        self.E382.setMouseTracking(False)
        self.E382.setStyleSheet(u"")
        self.E382.setAlignment(Qt.AlignCenter)
        self.E382.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_60.addWidget(self.E382)

        self.horizontalSpacer_108 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_60.addItem(self.horizontalSpacer_108)


        self.verticalLayout_12.addWidget(self.EL38)

        self.EL39 = QFrame(self.frame_19)
        self.EL39.setObjectName(u"EL39")
        self.EL39.setMinimumSize(QSize(0, 26))
        self.EL39.setMaximumSize(QSize(16777215, 26))
        self.EL39.setFrameShape(QFrame.StyledPanel)
        self.EL39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.EL39)
        self.horizontalLayout_59.setSpacing(0)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.label_77 = QLabel(self.EL39)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setMaximumSize(QSize(110, 16777215))
        self.label_77.setFont(font6)
        self.label_77.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_59.addWidget(self.label_77)

        self.horizontalSpacer_103 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_59.addItem(self.horizontalSpacer_103)

        self.E391 = QLineEdit(self.EL39)
        self.E391.setObjectName(u"E391")
        self.E391.setMinimumSize(QSize(50, 0))
        self.E391.setMaximumSize(QSize(50, 16777215))
        self.E391.setMouseTracking(False)
        self.E391.setStyleSheet(u"")
        self.E391.setAlignment(Qt.AlignCenter)
        self.E391.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_59.addWidget(self.E391)

        self.horizontalSpacer_104 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_59.addItem(self.horizontalSpacer_104)

        self.E392 = QLineEdit(self.EL39)
        self.E392.setObjectName(u"E392")
        self.E392.setMinimumSize(QSize(50, 0))
        self.E392.setMaximumSize(QSize(50, 16777215))
        self.E392.setMouseTracking(False)
        self.E392.setStyleSheet(u"")
        self.E392.setAlignment(Qt.AlignCenter)
        self.E392.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_59.addWidget(self.E392)

        self.horizontalSpacer_105 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_59.addItem(self.horizontalSpacer_105)


        self.verticalLayout_12.addWidget(self.EL39)

        self.EL40 = QFrame(self.frame_19)
        self.EL40.setObjectName(u"EL40")
        self.EL40.setMinimumSize(QSize(0, 26))
        self.EL40.setMaximumSize(QSize(16777215, 26))
        self.EL40.setFrameShape(QFrame.StyledPanel)
        self.EL40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.EL40)
        self.horizontalLayout_61.setSpacing(0)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.label_79 = QLabel(self.EL40)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setMaximumSize(QSize(110, 16777215))
        self.label_79.setFont(font6)
        self.label_79.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_61.addWidget(self.label_79)

        self.horizontalSpacer_109 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_61.addItem(self.horizontalSpacer_109)

        self.E401 = QLineEdit(self.EL40)
        self.E401.setObjectName(u"E401")
        self.E401.setMinimumSize(QSize(50, 0))
        self.E401.setMaximumSize(QSize(50, 16777215))
        self.E401.setMouseTracking(False)
        self.E401.setStyleSheet(u"")
        self.E401.setAlignment(Qt.AlignCenter)
        self.E401.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_61.addWidget(self.E401)

        self.horizontalSpacer_110 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_61.addItem(self.horizontalSpacer_110)

        self.E402 = QLineEdit(self.EL40)
        self.E402.setObjectName(u"E402")
        self.E402.setMinimumSize(QSize(50, 0))
        self.E402.setMaximumSize(QSize(50, 16777215))
        self.E402.setMouseTracking(False)
        self.E402.setStyleSheet(u"")
        self.E402.setAlignment(Qt.AlignCenter)
        self.E402.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_61.addWidget(self.E402)

        self.horizontalSpacer_111 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_61.addItem(self.horizontalSpacer_111)


        self.verticalLayout_12.addWidget(self.EL40)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_6)


        self.horizontalLayout_10.addWidget(self.frame_19)


        self.verticalLayout_11.addWidget(self.frame_18)

        self.frame_32 = QFrame(self.frame_17)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMaximumSize(QSize(16777215, 60))
        self.frame_32.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid rgb(38, 40, 61);\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_32.setFrameShape(QFrame.NoFrame)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 10)
        self.nextButtonIncidencias = QPushButton(self.frame_32)
        self.nextButtonIncidencias.setObjectName(u"nextButtonIncidencias")
        self.nextButtonIncidencias.setMinimumSize(QSize(0, 30))
        self.nextButtonIncidencias.setMaximumSize(QSize(150, 16777215))
        self.nextButtonIncidencias.setFont(font4)
        self.nextButtonIncidencias.setStyleSheet(u"QPushButton {\n"
"	padding-left: 5px;\n"
"	background-color: rgb(38, 40, 61);\n"
"	border:none;\n"
"	border-radius:15px;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 3px solid;\n"
"	background-color:rgb(241, 102, 55);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color:rgb(241, 102, 55);\n"
"}\n"
"")

        self.horizontalLayout_11.addWidget(self.nextButtonIncidencias)


        self.verticalLayout_11.addWidget(self.frame_32)


        self.horizontalLayout_9.addWidget(self.frame_17)

        self.stackedWidget.addWidget(self.Elementos)
        self.Liberdade = QWidget()
        self.Liberdade.setObjectName(u"Liberdade")
        self.horizontalLayout_54 = QHBoxLayout(self.Liberdade)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.frame_47 = QFrame(self.Liberdade)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setMinimumSize(QSize(500, 0))
        self.frame_47.setMaximumSize(QSize(1000, 500))
        self.frame_47.setFont(font)
        self.frame_47.setStyleSheet(u"QFrame{\n"
"background-color: rgb(148, 147, 150);\n"
"border-radius: 6px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: rgb(217, 217, 217);\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 5px;\n"
"    padding: 0px;\n"
"    font-size: 14px;\n"
"    color: #333;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color: rgb(217, 217, 217);\n"
"    border: 1px solid #66afe9;\n"
"    outline: none;\n"
"}")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_47)
        self.verticalLayout_16.setSpacing(15)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(-1, -1, -1, 30)
        self.frame_53 = QFrame(self.frame_47)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setMaximumSize(QSize(16777215, 40))
        self.frame_53.setFont(font1)
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_53)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_12 = QLabel(self.frame_53)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_12)


        self.verticalLayout_16.addWidget(self.frame_53)

        self.frame_21 = QFrame(self.frame_47)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_12.setSpacing(30)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_55 = QFrame(self.frame_21)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid rgb(38, 40, 61);\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_55)
        self.verticalLayout_18.setSpacing(6)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 5)
        self.frame_56 = QFrame(self.frame_55)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setMinimumSize(QSize(0, 40))
        self.frame_56.setMaximumSize(QSize(16777215, 40))
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_56)
        self.verticalLayout_19.setSpacing(3)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 10)
        self.frame_57 = QFrame(self.frame_56)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_36.setSpacing(40)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.label_54 = QLabel(self.frame_57)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setMinimumSize(QSize(50, 0))
        self.label_54.setMaximumSize(QSize(50, 16777215))
        self.label_54.setFont(font5)
        self.label_54.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_36.addWidget(self.label_54)

        self.label_60 = QLabel(self.frame_57)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setMinimumSize(QSize(50, 0))
        self.label_60.setMaximumSize(QSize(50, 16777215))
        self.label_60.setFont(font5)
        self.label_60.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_36.addWidget(self.label_60)

        self.label_62 = QLabel(self.frame_57)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setMinimumSize(QSize(50, 0))
        self.label_62.setMaximumSize(QSize(50, 16777215))
        self.label_62.setFont(font5)
        self.label_62.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_36.addWidget(self.label_62)

        self.label_73 = QLabel(self.frame_57)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setMinimumSize(QSize(50, 0))
        self.label_73.setMaximumSize(QSize(50, 16777215))
        self.label_73.setFont(font5)
        self.label_73.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_36.addWidget(self.label_73)


        self.verticalLayout_19.addWidget(self.frame_57)

        self.line_3 = QFrame(self.frame_56)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMinimumSize(QSize(0, 2))
        self.line_3.setMaximumSize(QSize(16777215, 2))
        self.line_3.setStyleSheet(u"border: 1px solid rgb(0, 0, 0);")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_19.addWidget(self.line_3)


        self.verticalLayout_18.addWidget(self.frame_56)

        self.GR1 = QFrame(self.frame_55)
        self.GR1.setObjectName(u"GR1")
        self.GR1.setMinimumSize(QSize(0, 38))
        self.GR1.setFrameShape(QFrame.StyledPanel)
        self.GR1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.GR1)
        self.horizontalLayout_42.setSpacing(40)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.label_63 = QLabel(self.GR1)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setMinimumSize(QSize(50, 0))
        self.label_63.setMaximumSize(QSize(50, 16777215))
        self.label_63.setFont(font6)
        self.label_63.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_42.addWidget(self.label_63)

        self.G11 = QLineEdit(self.GR1)
        self.G11.setObjectName(u"G11")
        self.G11.setMinimumSize(QSize(50, 0))
        self.G11.setMaximumSize(QSize(50, 16777215))
        self.G11.setMouseTracking(False)
        self.G11.setStyleSheet(u"")
        self.G11.setAlignment(Qt.AlignCenter)
        self.G11.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_42.addWidget(self.G11)

        self.G21 = QLineEdit(self.GR1)
        self.G21.setObjectName(u"G21")
        self.G21.setMinimumSize(QSize(50, 0))
        self.G21.setMaximumSize(QSize(50, 16777215))
        self.G21.setMouseTracking(False)
        self.G21.setStyleSheet(u"")
        self.G21.setAlignment(Qt.AlignCenter)
        self.G21.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_42.addWidget(self.G21)

        self.G31 = QLineEdit(self.GR1)
        self.G31.setObjectName(u"G31")
        self.G31.setMinimumSize(QSize(50, 0))
        self.G31.setMaximumSize(QSize(50, 16777215))
        self.G31.setMouseTracking(False)
        self.G31.setStyleSheet(u"")
        self.G31.setAlignment(Qt.AlignCenter)
        self.G31.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_42.addWidget(self.G31)


        self.verticalLayout_18.addWidget(self.GR1)

        self.GR2 = QFrame(self.frame_55)
        self.GR2.setObjectName(u"GR2")
        self.GR2.setMinimumSize(QSize(0, 38))
        self.GR2.setFrameShape(QFrame.StyledPanel)
        self.GR2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.GR2)
        self.horizontalLayout_44.setSpacing(40)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.label_64 = QLabel(self.GR2)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMinimumSize(QSize(50, 0))
        self.label_64.setMaximumSize(QSize(50, 16777215))
        self.label_64.setFont(font6)
        self.label_64.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_44.addWidget(self.label_64)

        self.G12 = QLineEdit(self.GR2)
        self.G12.setObjectName(u"G12")
        self.G12.setMinimumSize(QSize(50, 0))
        self.G12.setMaximumSize(QSize(50, 16777215))
        self.G12.setMouseTracking(False)
        self.G12.setStyleSheet(u"")
        self.G12.setAlignment(Qt.AlignCenter)
        self.G12.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_44.addWidget(self.G12)

        self.G22 = QLineEdit(self.GR2)
        self.G22.setObjectName(u"G22")
        self.G22.setMinimumSize(QSize(50, 0))
        self.G22.setMaximumSize(QSize(50, 16777215))
        self.G22.setMouseTracking(False)
        self.G22.setStyleSheet(u"")
        self.G22.setAlignment(Qt.AlignCenter)
        self.G22.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_44.addWidget(self.G22)

        self.G32 = QLineEdit(self.GR2)
        self.G32.setObjectName(u"G32")
        self.G32.setMinimumSize(QSize(50, 0))
        self.G32.setMaximumSize(QSize(50, 16777215))
        self.G32.setMouseTracking(False)
        self.G32.setStyleSheet(u"")
        self.G32.setAlignment(Qt.AlignCenter)
        self.G32.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_44.addWidget(self.G32)


        self.verticalLayout_18.addWidget(self.GR2)

        self.GR3 = QFrame(self.frame_55)
        self.GR3.setObjectName(u"GR3")
        self.GR3.setMinimumSize(QSize(0, 38))
        self.GR3.setFrameShape(QFrame.StyledPanel)
        self.GR3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.GR3)
        self.horizontalLayout_45.setSpacing(40)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.label_65 = QLabel(self.GR3)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setMinimumSize(QSize(50, 0))
        self.label_65.setMaximumSize(QSize(50, 16777215))
        self.label_65.setFont(font6)
        self.label_65.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_45.addWidget(self.label_65)

        self.G13 = QLineEdit(self.GR3)
        self.G13.setObjectName(u"G13")
        self.G13.setMinimumSize(QSize(50, 0))
        self.G13.setMaximumSize(QSize(50, 16777215))
        self.G13.setMouseTracking(False)
        self.G13.setStyleSheet(u"")
        self.G13.setAlignment(Qt.AlignCenter)
        self.G13.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_45.addWidget(self.G13)

        self.G23 = QLineEdit(self.GR3)
        self.G23.setObjectName(u"G23")
        self.G23.setMinimumSize(QSize(50, 0))
        self.G23.setMaximumSize(QSize(50, 16777215))
        self.G23.setMouseTracking(False)
        self.G23.setStyleSheet(u"")
        self.G23.setAlignment(Qt.AlignCenter)
        self.G23.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_45.addWidget(self.G23)

        self.G33 = QLineEdit(self.GR3)
        self.G33.setObjectName(u"G33")
        self.G33.setMinimumSize(QSize(50, 0))
        self.G33.setMaximumSize(QSize(50, 16777215))
        self.G33.setMouseTracking(False)
        self.G33.setStyleSheet(u"")
        self.G33.setAlignment(Qt.AlignCenter)
        self.G33.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_45.addWidget(self.G33)


        self.verticalLayout_18.addWidget(self.GR3)

        self.GR4 = QFrame(self.frame_55)
        self.GR4.setObjectName(u"GR4")
        self.GR4.setMinimumSize(QSize(0, 38))
        self.GR4.setFrameShape(QFrame.StyledPanel)
        self.GR4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.GR4)
        self.horizontalLayout_46.setSpacing(40)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.label_66 = QLabel(self.GR4)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMinimumSize(QSize(50, 0))
        self.label_66.setMaximumSize(QSize(50, 16777215))
        self.label_66.setFont(font6)
        self.label_66.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_46.addWidget(self.label_66)

        self.G14 = QLineEdit(self.GR4)
        self.G14.setObjectName(u"G14")
        self.G14.setMinimumSize(QSize(50, 0))
        self.G14.setMaximumSize(QSize(50, 16777215))
        self.G14.setMouseTracking(False)
        self.G14.setStyleSheet(u"")
        self.G14.setAlignment(Qt.AlignCenter)
        self.G14.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_46.addWidget(self.G14)

        self.G24 = QLineEdit(self.GR4)
        self.G24.setObjectName(u"G24")
        self.G24.setMinimumSize(QSize(50, 0))
        self.G24.setMaximumSize(QSize(50, 16777215))
        self.G24.setMouseTracking(False)
        self.G24.setStyleSheet(u"")
        self.G24.setAlignment(Qt.AlignCenter)
        self.G24.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_46.addWidget(self.G24)

        self.G34 = QLineEdit(self.GR4)
        self.G34.setObjectName(u"G34")
        self.G34.setMinimumSize(QSize(50, 0))
        self.G34.setMaximumSize(QSize(50, 16777215))
        self.G34.setMouseTracking(False)
        self.G34.setStyleSheet(u"")
        self.G34.setAlignment(Qt.AlignCenter)
        self.G34.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_46.addWidget(self.G34)


        self.verticalLayout_18.addWidget(self.GR4)

        self.GR5 = QFrame(self.frame_55)
        self.GR5.setObjectName(u"GR5")
        self.GR5.setMinimumSize(QSize(0, 38))
        self.GR5.setFrameShape(QFrame.StyledPanel)
        self.GR5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.GR5)
        self.horizontalLayout_47.setSpacing(40)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.label_67 = QLabel(self.GR5)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setMinimumSize(QSize(50, 0))
        self.label_67.setMaximumSize(QSize(50, 16777215))
        self.label_67.setFont(font6)
        self.label_67.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_47.addWidget(self.label_67)

        self.G15 = QLineEdit(self.GR5)
        self.G15.setObjectName(u"G15")
        self.G15.setMinimumSize(QSize(50, 0))
        self.G15.setMaximumSize(QSize(50, 16777215))
        self.G15.setMouseTracking(False)
        self.G15.setStyleSheet(u"")
        self.G15.setAlignment(Qt.AlignCenter)
        self.G15.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_47.addWidget(self.G15)

        self.G25 = QLineEdit(self.GR5)
        self.G25.setObjectName(u"G25")
        self.G25.setMinimumSize(QSize(50, 0))
        self.G25.setMaximumSize(QSize(50, 16777215))
        self.G25.setMouseTracking(False)
        self.G25.setStyleSheet(u"")
        self.G25.setAlignment(Qt.AlignCenter)
        self.G25.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_47.addWidget(self.G25)

        self.G35 = QLineEdit(self.GR5)
        self.G35.setObjectName(u"G35")
        self.G35.setMinimumSize(QSize(50, 0))
        self.G35.setMaximumSize(QSize(50, 16777215))
        self.G35.setMouseTracking(False)
        self.G35.setStyleSheet(u"")
        self.G35.setAlignment(Qt.AlignCenter)
        self.G35.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_47.addWidget(self.G35)


        self.verticalLayout_18.addWidget(self.GR5)

        self.GR6 = QFrame(self.frame_55)
        self.GR6.setObjectName(u"GR6")
        self.GR6.setMinimumSize(QSize(0, 38))
        self.GR6.setFrameShape(QFrame.StyledPanel)
        self.GR6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.GR6)
        self.horizontalLayout_48.setSpacing(40)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.label_68 = QLabel(self.GR6)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setMinimumSize(QSize(50, 0))
        self.label_68.setMaximumSize(QSize(50, 16777215))
        self.label_68.setFont(font6)
        self.label_68.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_48.addWidget(self.label_68)

        self.G16 = QLineEdit(self.GR6)
        self.G16.setObjectName(u"G16")
        self.G16.setMinimumSize(QSize(50, 0))
        self.G16.setMaximumSize(QSize(50, 16777215))
        self.G16.setMouseTracking(False)
        self.G16.setStyleSheet(u"")
        self.G16.setAlignment(Qt.AlignCenter)
        self.G16.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_48.addWidget(self.G16)

        self.G26 = QLineEdit(self.GR6)
        self.G26.setObjectName(u"G26")
        self.G26.setMinimumSize(QSize(50, 0))
        self.G26.setMaximumSize(QSize(50, 16777215))
        self.G26.setMouseTracking(False)
        self.G26.setStyleSheet(u"")
        self.G26.setAlignment(Qt.AlignCenter)
        self.G26.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_48.addWidget(self.G26)

        self.G36 = QLineEdit(self.GR6)
        self.G36.setObjectName(u"G36")
        self.G36.setMinimumSize(QSize(50, 0))
        self.G36.setMaximumSize(QSize(50, 16777215))
        self.G36.setMouseTracking(False)
        self.G36.setStyleSheet(u"")
        self.G36.setAlignment(Qt.AlignCenter)
        self.G36.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_48.addWidget(self.G36)


        self.verticalLayout_18.addWidget(self.GR6)

        self.GR7 = QFrame(self.frame_55)
        self.GR7.setObjectName(u"GR7")
        self.GR7.setMinimumSize(QSize(0, 38))
        self.GR7.setFrameShape(QFrame.StyledPanel)
        self.GR7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.GR7)
        self.horizontalLayout_49.setSpacing(40)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.label_69 = QLabel(self.GR7)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setMinimumSize(QSize(50, 0))
        self.label_69.setMaximumSize(QSize(50, 16777215))
        self.label_69.setFont(font6)
        self.label_69.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_49.addWidget(self.label_69)

        self.G17 = QLineEdit(self.GR7)
        self.G17.setObjectName(u"G17")
        self.G17.setMinimumSize(QSize(50, 0))
        self.G17.setMaximumSize(QSize(50, 16777215))
        self.G17.setMouseTracking(False)
        self.G17.setStyleSheet(u"")
        self.G17.setAlignment(Qt.AlignCenter)
        self.G17.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_49.addWidget(self.G17)

        self.G27 = QLineEdit(self.GR7)
        self.G27.setObjectName(u"G27")
        self.G27.setMinimumSize(QSize(50, 0))
        self.G27.setMaximumSize(QSize(50, 16777215))
        self.G27.setMouseTracking(False)
        self.G27.setStyleSheet(u"")
        self.G27.setAlignment(Qt.AlignCenter)
        self.G27.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_49.addWidget(self.G27)

        self.G37 = QLineEdit(self.GR7)
        self.G37.setObjectName(u"G37")
        self.G37.setMinimumSize(QSize(50, 0))
        self.G37.setMaximumSize(QSize(50, 16777215))
        self.G37.setMouseTracking(False)
        self.G37.setStyleSheet(u"")
        self.G37.setAlignment(Qt.AlignCenter)
        self.G37.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_49.addWidget(self.G37)


        self.verticalLayout_18.addWidget(self.GR7)

        self.GR8 = QFrame(self.frame_55)
        self.GR8.setObjectName(u"GR8")
        self.GR8.setMinimumSize(QSize(0, 38))
        self.GR8.setFrameShape(QFrame.StyledPanel)
        self.GR8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.GR8)
        self.horizontalLayout_50.setSpacing(40)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.label_70 = QLabel(self.GR8)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setMinimumSize(QSize(50, 0))
        self.label_70.setMaximumSize(QSize(50, 16777215))
        self.label_70.setFont(font6)
        self.label_70.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_50.addWidget(self.label_70)

        self.G18 = QLineEdit(self.GR8)
        self.G18.setObjectName(u"G18")
        self.G18.setMinimumSize(QSize(50, 0))
        self.G18.setMaximumSize(QSize(50, 16777215))
        self.G18.setMouseTracking(False)
        self.G18.setStyleSheet(u"")
        self.G18.setAlignment(Qt.AlignCenter)
        self.G18.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_50.addWidget(self.G18)

        self.G28 = QLineEdit(self.GR8)
        self.G28.setObjectName(u"G28")
        self.G28.setMinimumSize(QSize(50, 0))
        self.G28.setMaximumSize(QSize(50, 16777215))
        self.G28.setMouseTracking(False)
        self.G28.setStyleSheet(u"")
        self.G28.setAlignment(Qt.AlignCenter)
        self.G28.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_50.addWidget(self.G28)

        self.G38 = QLineEdit(self.GR8)
        self.G38.setObjectName(u"G38")
        self.G38.setMinimumSize(QSize(50, 0))
        self.G38.setMaximumSize(QSize(50, 16777215))
        self.G38.setMouseTracking(False)
        self.G38.setStyleSheet(u"")
        self.G38.setAlignment(Qt.AlignCenter)
        self.G38.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_50.addWidget(self.G38)


        self.verticalLayout_18.addWidget(self.GR8)

        self.GR9 = QFrame(self.frame_55)
        self.GR9.setObjectName(u"GR9")
        self.GR9.setMinimumSize(QSize(0, 38))
        self.GR9.setFrameShape(QFrame.StyledPanel)
        self.GR9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.GR9)
        self.horizontalLayout_51.setSpacing(40)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.label_71 = QLabel(self.GR9)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setMinimumSize(QSize(50, 0))
        self.label_71.setMaximumSize(QSize(50, 16777215))
        self.label_71.setFont(font6)
        self.label_71.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_51.addWidget(self.label_71)

        self.G19 = QLineEdit(self.GR9)
        self.G19.setObjectName(u"G19")
        self.G19.setMinimumSize(QSize(50, 0))
        self.G19.setMaximumSize(QSize(50, 16777215))
        self.G19.setMouseTracking(False)
        self.G19.setStyleSheet(u"")
        self.G19.setAlignment(Qt.AlignCenter)
        self.G19.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_51.addWidget(self.G19)

        self.G29 = QLineEdit(self.GR9)
        self.G29.setObjectName(u"G29")
        self.G29.setMinimumSize(QSize(50, 0))
        self.G29.setMaximumSize(QSize(50, 16777215))
        self.G29.setMouseTracking(False)
        self.G29.setStyleSheet(u"")
        self.G29.setAlignment(Qt.AlignCenter)
        self.G29.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_51.addWidget(self.G29)

        self.G39 = QLineEdit(self.GR9)
        self.G39.setObjectName(u"G39")
        self.G39.setMinimumSize(QSize(50, 0))
        self.G39.setMaximumSize(QSize(50, 16777215))
        self.G39.setMouseTracking(False)
        self.G39.setStyleSheet(u"")
        self.G39.setAlignment(Qt.AlignCenter)
        self.G39.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_51.addWidget(self.G39)


        self.verticalLayout_18.addWidget(self.GR9)

        self.GR10 = QFrame(self.frame_55)
        self.GR10.setObjectName(u"GR10")
        self.GR10.setMinimumSize(QSize(0, 38))
        self.GR10.setFrameShape(QFrame.StyledPanel)
        self.GR10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.GR10)
        self.horizontalLayout_52.setSpacing(40)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.label_72 = QLabel(self.GR10)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setMinimumSize(QSize(50, 0))
        self.label_72.setMaximumSize(QSize(50, 16777215))
        self.label_72.setFont(font6)
        self.label_72.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_52.addWidget(self.label_72)

        self.G110 = QLineEdit(self.GR10)
        self.G110.setObjectName(u"G110")
        self.G110.setMinimumSize(QSize(50, 0))
        self.G110.setMaximumSize(QSize(50, 16777215))
        self.G110.setMouseTracking(False)
        self.G110.setStyleSheet(u"")
        self.G110.setAlignment(Qt.AlignCenter)
        self.G110.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_52.addWidget(self.G110)

        self.G210 = QLineEdit(self.GR10)
        self.G210.setObjectName(u"G210")
        self.G210.setMinimumSize(QSize(50, 0))
        self.G210.setMaximumSize(QSize(50, 16777215))
        self.G210.setMouseTracking(False)
        self.G210.setStyleSheet(u"")
        self.G210.setAlignment(Qt.AlignCenter)
        self.G210.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_52.addWidget(self.G210)

        self.G310 = QLineEdit(self.GR10)
        self.G310.setObjectName(u"G310")
        self.G310.setMinimumSize(QSize(50, 0))
        self.G310.setMaximumSize(QSize(50, 16777215))
        self.G310.setMouseTracking(False)
        self.G310.setStyleSheet(u"")
        self.G310.setAlignment(Qt.AlignCenter)
        self.G310.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_52.addWidget(self.G310)


        self.verticalLayout_18.addWidget(self.GR10)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_8)


        self.horizontalLayout_12.addWidget(self.frame_55)

        self.frame_127 = QFrame(self.frame_21)
        self.frame_127.setObjectName(u"frame_127")
        self.frame_127.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid rgb(38, 40, 61);\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_127.setFrameShape(QFrame.StyledPanel)
        self.frame_127.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_127)
        self.verticalLayout_32.setSpacing(6)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 5)
        self.frame_128 = QFrame(self.frame_127)
        self.frame_128.setObjectName(u"frame_128")
        self.frame_128.setMinimumSize(QSize(0, 40))
        self.frame_128.setMaximumSize(QSize(16777215, 40))
        self.frame_128.setFrameShape(QFrame.StyledPanel)
        self.frame_128.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_128)
        self.verticalLayout_33.setSpacing(3)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 10)
        self.frame_129 = QFrame(self.frame_128)
        self.frame_129.setObjectName(u"frame_129")
        self.frame_129.setFrameShape(QFrame.StyledPanel)
        self.frame_129.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_115 = QHBoxLayout(self.frame_129)
        self.horizontalLayout_115.setSpacing(40)
        self.horizontalLayout_115.setObjectName(u"horizontalLayout_115")
        self.horizontalLayout_115.setContentsMargins(0, 0, 0, 0)
        self.label_140 = QLabel(self.frame_129)
        self.label_140.setObjectName(u"label_140")
        self.label_140.setMinimumSize(QSize(50, 0))
        self.label_140.setMaximumSize(QSize(50, 16777215))
        self.label_140.setFont(font5)
        self.label_140.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_115.addWidget(self.label_140)

        self.label_141 = QLabel(self.frame_129)
        self.label_141.setObjectName(u"label_141")
        self.label_141.setMinimumSize(QSize(50, 0))
        self.label_141.setMaximumSize(QSize(50, 16777215))
        self.label_141.setFont(font5)
        self.label_141.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_115.addWidget(self.label_141)

        self.label_142 = QLabel(self.frame_129)
        self.label_142.setObjectName(u"label_142")
        self.label_142.setMinimumSize(QSize(50, 0))
        self.label_142.setMaximumSize(QSize(50, 16777215))
        self.label_142.setFont(font5)
        self.label_142.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_115.addWidget(self.label_142)

        self.label_143 = QLabel(self.frame_129)
        self.label_143.setObjectName(u"label_143")
        self.label_143.setMinimumSize(QSize(50, 0))
        self.label_143.setMaximumSize(QSize(50, 16777215))
        self.label_143.setFont(font5)
        self.label_143.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_115.addWidget(self.label_143)


        self.verticalLayout_33.addWidget(self.frame_129)

        self.line_9 = QFrame(self.frame_128)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setMinimumSize(QSize(0, 2))
        self.line_9.setMaximumSize(QSize(16777215, 2))
        self.line_9.setStyleSheet(u"border: 1px solid rgb(0, 0, 0);")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_33.addWidget(self.line_9)


        self.verticalLayout_32.addWidget(self.frame_128)

        self.GR11 = QFrame(self.frame_127)
        self.GR11.setObjectName(u"GR11")
        self.GR11.setMinimumSize(QSize(0, 38))
        self.GR11.setFrameShape(QFrame.StyledPanel)
        self.GR11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_116 = QHBoxLayout(self.GR11)
        self.horizontalLayout_116.setSpacing(40)
        self.horizontalLayout_116.setObjectName(u"horizontalLayout_116")
        self.horizontalLayout_116.setContentsMargins(0, 0, 0, 0)
        self.label_144 = QLabel(self.GR11)
        self.label_144.setObjectName(u"label_144")
        self.label_144.setMinimumSize(QSize(50, 0))
        self.label_144.setMaximumSize(QSize(50, 16777215))
        self.label_144.setFont(font6)
        self.label_144.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_116.addWidget(self.label_144)

        self.G111 = QLineEdit(self.GR11)
        self.G111.setObjectName(u"G111")
        self.G111.setMinimumSize(QSize(50, 0))
        self.G111.setMaximumSize(QSize(50, 16777215))
        self.G111.setMouseTracking(False)
        self.G111.setStyleSheet(u"")
        self.G111.setAlignment(Qt.AlignCenter)
        self.G111.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_116.addWidget(self.G111)

        self.G211 = QLineEdit(self.GR11)
        self.G211.setObjectName(u"G211")
        self.G211.setMinimumSize(QSize(50, 0))
        self.G211.setMaximumSize(QSize(50, 16777215))
        self.G211.setMouseTracking(False)
        self.G211.setStyleSheet(u"")
        self.G211.setAlignment(Qt.AlignCenter)
        self.G211.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_116.addWidget(self.G211)

        self.G311 = QLineEdit(self.GR11)
        self.G311.setObjectName(u"G311")
        self.G311.setMinimumSize(QSize(50, 0))
        self.G311.setMaximumSize(QSize(50, 16777215))
        self.G311.setMouseTracking(False)
        self.G311.setStyleSheet(u"")
        self.G311.setAlignment(Qt.AlignCenter)
        self.G311.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_116.addWidget(self.G311)


        self.verticalLayout_32.addWidget(self.GR11)

        self.GR12 = QFrame(self.frame_127)
        self.GR12.setObjectName(u"GR12")
        self.GR12.setMinimumSize(QSize(0, 38))
        self.GR12.setFrameShape(QFrame.StyledPanel)
        self.GR12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_117 = QHBoxLayout(self.GR12)
        self.horizontalLayout_117.setSpacing(40)
        self.horizontalLayout_117.setObjectName(u"horizontalLayout_117")
        self.horizontalLayout_117.setContentsMargins(0, 0, 0, 0)
        self.label_145 = QLabel(self.GR12)
        self.label_145.setObjectName(u"label_145")
        self.label_145.setMinimumSize(QSize(50, 0))
        self.label_145.setMaximumSize(QSize(50, 16777215))
        self.label_145.setFont(font6)
        self.label_145.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_117.addWidget(self.label_145)

        self.G112 = QLineEdit(self.GR12)
        self.G112.setObjectName(u"G112")
        self.G112.setMinimumSize(QSize(50, 0))
        self.G112.setMaximumSize(QSize(50, 16777215))
        self.G112.setMouseTracking(False)
        self.G112.setStyleSheet(u"")
        self.G112.setAlignment(Qt.AlignCenter)
        self.G112.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_117.addWidget(self.G112)

        self.G212 = QLineEdit(self.GR12)
        self.G212.setObjectName(u"G212")
        self.G212.setMinimumSize(QSize(50, 0))
        self.G212.setMaximumSize(QSize(50, 16777215))
        self.G212.setMouseTracking(False)
        self.G212.setStyleSheet(u"")
        self.G212.setAlignment(Qt.AlignCenter)
        self.G212.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_117.addWidget(self.G212)

        self.G312 = QLineEdit(self.GR12)
        self.G312.setObjectName(u"G312")
        self.G312.setMinimumSize(QSize(50, 0))
        self.G312.setMaximumSize(QSize(50, 16777215))
        self.G312.setMouseTracking(False)
        self.G312.setStyleSheet(u"")
        self.G312.setAlignment(Qt.AlignCenter)
        self.G312.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_117.addWidget(self.G312)


        self.verticalLayout_32.addWidget(self.GR12)

        self.GR13 = QFrame(self.frame_127)
        self.GR13.setObjectName(u"GR13")
        self.GR13.setMinimumSize(QSize(0, 38))
        self.GR13.setFrameShape(QFrame.StyledPanel)
        self.GR13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_118 = QHBoxLayout(self.GR13)
        self.horizontalLayout_118.setSpacing(40)
        self.horizontalLayout_118.setObjectName(u"horizontalLayout_118")
        self.horizontalLayout_118.setContentsMargins(0, 0, 0, 0)
        self.label_146 = QLabel(self.GR13)
        self.label_146.setObjectName(u"label_146")
        self.label_146.setMinimumSize(QSize(50, 0))
        self.label_146.setMaximumSize(QSize(50, 16777215))
        self.label_146.setFont(font6)
        self.label_146.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_118.addWidget(self.label_146)

        self.G113 = QLineEdit(self.GR13)
        self.G113.setObjectName(u"G113")
        self.G113.setMinimumSize(QSize(50, 0))
        self.G113.setMaximumSize(QSize(50, 16777215))
        self.G113.setMouseTracking(False)
        self.G113.setStyleSheet(u"")
        self.G113.setAlignment(Qt.AlignCenter)
        self.G113.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_118.addWidget(self.G113)

        self.G213 = QLineEdit(self.GR13)
        self.G213.setObjectName(u"G213")
        self.G213.setMinimumSize(QSize(50, 0))
        self.G213.setMaximumSize(QSize(50, 16777215))
        self.G213.setMouseTracking(False)
        self.G213.setStyleSheet(u"")
        self.G213.setAlignment(Qt.AlignCenter)
        self.G213.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_118.addWidget(self.G213)

        self.G313 = QLineEdit(self.GR13)
        self.G313.setObjectName(u"G313")
        self.G313.setMinimumSize(QSize(50, 0))
        self.G313.setMaximumSize(QSize(50, 16777215))
        self.G313.setMouseTracking(False)
        self.G313.setStyleSheet(u"")
        self.G313.setAlignment(Qt.AlignCenter)
        self.G313.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_118.addWidget(self.G313)


        self.verticalLayout_32.addWidget(self.GR13)

        self.GR14 = QFrame(self.frame_127)
        self.GR14.setObjectName(u"GR14")
        self.GR14.setMinimumSize(QSize(0, 38))
        self.GR14.setFrameShape(QFrame.StyledPanel)
        self.GR14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_119 = QHBoxLayout(self.GR14)
        self.horizontalLayout_119.setSpacing(40)
        self.horizontalLayout_119.setObjectName(u"horizontalLayout_119")
        self.horizontalLayout_119.setContentsMargins(0, 0, 0, 0)
        self.label_147 = QLabel(self.GR14)
        self.label_147.setObjectName(u"label_147")
        self.label_147.setMinimumSize(QSize(50, 0))
        self.label_147.setMaximumSize(QSize(50, 16777215))
        self.label_147.setFont(font6)
        self.label_147.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_119.addWidget(self.label_147)

        self.G114 = QLineEdit(self.GR14)
        self.G114.setObjectName(u"G114")
        self.G114.setMinimumSize(QSize(50, 0))
        self.G114.setMaximumSize(QSize(50, 16777215))
        self.G114.setMouseTracking(False)
        self.G114.setStyleSheet(u"")
        self.G114.setAlignment(Qt.AlignCenter)
        self.G114.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_119.addWidget(self.G114)

        self.G214 = QLineEdit(self.GR14)
        self.G214.setObjectName(u"G214")
        self.G214.setMinimumSize(QSize(50, 0))
        self.G214.setMaximumSize(QSize(50, 16777215))
        self.G214.setMouseTracking(False)
        self.G214.setStyleSheet(u"")
        self.G214.setAlignment(Qt.AlignCenter)
        self.G214.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_119.addWidget(self.G214)

        self.G314 = QLineEdit(self.GR14)
        self.G314.setObjectName(u"G314")
        self.G314.setMinimumSize(QSize(50, 0))
        self.G314.setMaximumSize(QSize(50, 16777215))
        self.G314.setMouseTracking(False)
        self.G314.setStyleSheet(u"")
        self.G314.setAlignment(Qt.AlignCenter)
        self.G314.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_119.addWidget(self.G314)


        self.verticalLayout_32.addWidget(self.GR14)

        self.GR15 = QFrame(self.frame_127)
        self.GR15.setObjectName(u"GR15")
        self.GR15.setMinimumSize(QSize(0, 38))
        self.GR15.setFrameShape(QFrame.StyledPanel)
        self.GR15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_120 = QHBoxLayout(self.GR15)
        self.horizontalLayout_120.setSpacing(40)
        self.horizontalLayout_120.setObjectName(u"horizontalLayout_120")
        self.horizontalLayout_120.setContentsMargins(0, 0, 0, 0)
        self.label_148 = QLabel(self.GR15)
        self.label_148.setObjectName(u"label_148")
        self.label_148.setMinimumSize(QSize(50, 0))
        self.label_148.setMaximumSize(QSize(50, 16777215))
        self.label_148.setFont(font6)
        self.label_148.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_120.addWidget(self.label_148)

        self.G115 = QLineEdit(self.GR15)
        self.G115.setObjectName(u"G115")
        self.G115.setMinimumSize(QSize(50, 0))
        self.G115.setMaximumSize(QSize(50, 16777215))
        self.G115.setMouseTracking(False)
        self.G115.setStyleSheet(u"")
        self.G115.setAlignment(Qt.AlignCenter)
        self.G115.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_120.addWidget(self.G115)

        self.G215 = QLineEdit(self.GR15)
        self.G215.setObjectName(u"G215")
        self.G215.setMinimumSize(QSize(50, 0))
        self.G215.setMaximumSize(QSize(50, 16777215))
        self.G215.setMouseTracking(False)
        self.G215.setStyleSheet(u"")
        self.G215.setAlignment(Qt.AlignCenter)
        self.G215.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_120.addWidget(self.G215)

        self.G315 = QLineEdit(self.GR15)
        self.G315.setObjectName(u"G315")
        self.G315.setMinimumSize(QSize(50, 0))
        self.G315.setMaximumSize(QSize(50, 16777215))
        self.G315.setMouseTracking(False)
        self.G315.setStyleSheet(u"")
        self.G315.setAlignment(Qt.AlignCenter)
        self.G315.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_120.addWidget(self.G315)


        self.verticalLayout_32.addWidget(self.GR15)

        self.GR16 = QFrame(self.frame_127)
        self.GR16.setObjectName(u"GR16")
        self.GR16.setMinimumSize(QSize(0, 38))
        self.GR16.setFrameShape(QFrame.StyledPanel)
        self.GR16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_121 = QHBoxLayout(self.GR16)
        self.horizontalLayout_121.setSpacing(40)
        self.horizontalLayout_121.setObjectName(u"horizontalLayout_121")
        self.horizontalLayout_121.setContentsMargins(0, 0, 0, 0)
        self.label_149 = QLabel(self.GR16)
        self.label_149.setObjectName(u"label_149")
        self.label_149.setMinimumSize(QSize(50, 0))
        self.label_149.setMaximumSize(QSize(50, 16777215))
        self.label_149.setFont(font6)
        self.label_149.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_121.addWidget(self.label_149)

        self.G116 = QLineEdit(self.GR16)
        self.G116.setObjectName(u"G116")
        self.G116.setMinimumSize(QSize(50, 0))
        self.G116.setMaximumSize(QSize(50, 16777215))
        self.G116.setMouseTracking(False)
        self.G116.setStyleSheet(u"")
        self.G116.setAlignment(Qt.AlignCenter)
        self.G116.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_121.addWidget(self.G116)

        self.G216 = QLineEdit(self.GR16)
        self.G216.setObjectName(u"G216")
        self.G216.setMinimumSize(QSize(50, 0))
        self.G216.setMaximumSize(QSize(50, 16777215))
        self.G216.setMouseTracking(False)
        self.G216.setStyleSheet(u"")
        self.G216.setAlignment(Qt.AlignCenter)
        self.G216.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_121.addWidget(self.G216)

        self.G316 = QLineEdit(self.GR16)
        self.G316.setObjectName(u"G316")
        self.G316.setMinimumSize(QSize(50, 0))
        self.G316.setMaximumSize(QSize(50, 16777215))
        self.G316.setMouseTracking(False)
        self.G316.setStyleSheet(u"")
        self.G316.setAlignment(Qt.AlignCenter)
        self.G316.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_121.addWidget(self.G316)


        self.verticalLayout_32.addWidget(self.GR16)

        self.GR17 = QFrame(self.frame_127)
        self.GR17.setObjectName(u"GR17")
        self.GR17.setMinimumSize(QSize(0, 38))
        self.GR17.setFrameShape(QFrame.StyledPanel)
        self.GR17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_122 = QHBoxLayout(self.GR17)
        self.horizontalLayout_122.setSpacing(40)
        self.horizontalLayout_122.setObjectName(u"horizontalLayout_122")
        self.horizontalLayout_122.setContentsMargins(0, 0, 0, 0)
        self.label_150 = QLabel(self.GR17)
        self.label_150.setObjectName(u"label_150")
        self.label_150.setMinimumSize(QSize(50, 0))
        self.label_150.setMaximumSize(QSize(50, 16777215))
        self.label_150.setFont(font6)
        self.label_150.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_122.addWidget(self.label_150)

        self.G117 = QLineEdit(self.GR17)
        self.G117.setObjectName(u"G117")
        self.G117.setMinimumSize(QSize(50, 0))
        self.G117.setMaximumSize(QSize(50, 16777215))
        self.G117.setMouseTracking(False)
        self.G117.setStyleSheet(u"")
        self.G117.setAlignment(Qt.AlignCenter)
        self.G117.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_122.addWidget(self.G117)

        self.G217 = QLineEdit(self.GR17)
        self.G217.setObjectName(u"G217")
        self.G217.setMinimumSize(QSize(50, 0))
        self.G217.setMaximumSize(QSize(50, 16777215))
        self.G217.setMouseTracking(False)
        self.G217.setStyleSheet(u"")
        self.G217.setAlignment(Qt.AlignCenter)
        self.G217.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_122.addWidget(self.G217)

        self.G317 = QLineEdit(self.GR17)
        self.G317.setObjectName(u"G317")
        self.G317.setMinimumSize(QSize(50, 0))
        self.G317.setMaximumSize(QSize(50, 16777215))
        self.G317.setMouseTracking(False)
        self.G317.setStyleSheet(u"")
        self.G317.setAlignment(Qt.AlignCenter)
        self.G317.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_122.addWidget(self.G317)


        self.verticalLayout_32.addWidget(self.GR17)

        self.GR18 = QFrame(self.frame_127)
        self.GR18.setObjectName(u"GR18")
        self.GR18.setMinimumSize(QSize(0, 38))
        self.GR18.setFrameShape(QFrame.StyledPanel)
        self.GR18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_123 = QHBoxLayout(self.GR18)
        self.horizontalLayout_123.setSpacing(40)
        self.horizontalLayout_123.setObjectName(u"horizontalLayout_123")
        self.horizontalLayout_123.setContentsMargins(0, 0, 0, 0)
        self.label_151 = QLabel(self.GR18)
        self.label_151.setObjectName(u"label_151")
        self.label_151.setMinimumSize(QSize(50, 0))
        self.label_151.setMaximumSize(QSize(50, 16777215))
        self.label_151.setFont(font6)
        self.label_151.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_123.addWidget(self.label_151)

        self.G118 = QLineEdit(self.GR18)
        self.G118.setObjectName(u"G118")
        self.G118.setMinimumSize(QSize(50, 0))
        self.G118.setMaximumSize(QSize(50, 16777215))
        self.G118.setMouseTracking(False)
        self.G118.setStyleSheet(u"")
        self.G118.setAlignment(Qt.AlignCenter)
        self.G118.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_123.addWidget(self.G118)

        self.G218 = QLineEdit(self.GR18)
        self.G218.setObjectName(u"G218")
        self.G218.setMinimumSize(QSize(50, 0))
        self.G218.setMaximumSize(QSize(50, 16777215))
        self.G218.setMouseTracking(False)
        self.G218.setStyleSheet(u"")
        self.G218.setAlignment(Qt.AlignCenter)
        self.G218.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_123.addWidget(self.G218)

        self.G318 = QLineEdit(self.GR18)
        self.G318.setObjectName(u"G318")
        self.G318.setMinimumSize(QSize(50, 0))
        self.G318.setMaximumSize(QSize(50, 16777215))
        self.G318.setMouseTracking(False)
        self.G318.setStyleSheet(u"")
        self.G318.setAlignment(Qt.AlignCenter)
        self.G318.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_123.addWidget(self.G318)


        self.verticalLayout_32.addWidget(self.GR18)

        self.GR19 = QFrame(self.frame_127)
        self.GR19.setObjectName(u"GR19")
        self.GR19.setMinimumSize(QSize(0, 38))
        self.GR19.setFrameShape(QFrame.StyledPanel)
        self.GR19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_124 = QHBoxLayout(self.GR19)
        self.horizontalLayout_124.setSpacing(40)
        self.horizontalLayout_124.setObjectName(u"horizontalLayout_124")
        self.horizontalLayout_124.setContentsMargins(0, 0, 0, 0)
        self.label_152 = QLabel(self.GR19)
        self.label_152.setObjectName(u"label_152")
        self.label_152.setMinimumSize(QSize(50, 0))
        self.label_152.setMaximumSize(QSize(50, 16777215))
        self.label_152.setFont(font6)
        self.label_152.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_124.addWidget(self.label_152)

        self.G119 = QLineEdit(self.GR19)
        self.G119.setObjectName(u"G119")
        self.G119.setMinimumSize(QSize(50, 0))
        self.G119.setMaximumSize(QSize(50, 16777215))
        self.G119.setMouseTracking(False)
        self.G119.setStyleSheet(u"")
        self.G119.setAlignment(Qt.AlignCenter)
        self.G119.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_124.addWidget(self.G119)

        self.G219 = QLineEdit(self.GR19)
        self.G219.setObjectName(u"G219")
        self.G219.setMinimumSize(QSize(50, 0))
        self.G219.setMaximumSize(QSize(50, 16777215))
        self.G219.setMouseTracking(False)
        self.G219.setStyleSheet(u"")
        self.G219.setAlignment(Qt.AlignCenter)
        self.G219.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_124.addWidget(self.G219)

        self.G319 = QLineEdit(self.GR19)
        self.G319.setObjectName(u"G319")
        self.G319.setMinimumSize(QSize(50, 0))
        self.G319.setMaximumSize(QSize(50, 16777215))
        self.G319.setMouseTracking(False)
        self.G319.setStyleSheet(u"")
        self.G319.setAlignment(Qt.AlignCenter)
        self.G319.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_124.addWidget(self.G319)


        self.verticalLayout_32.addWidget(self.GR19)

        self.GR20 = QFrame(self.frame_127)
        self.GR20.setObjectName(u"GR20")
        self.GR20.setMinimumSize(QSize(0, 38))
        self.GR20.setFrameShape(QFrame.StyledPanel)
        self.GR20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_125 = QHBoxLayout(self.GR20)
        self.horizontalLayout_125.setSpacing(40)
        self.horizontalLayout_125.setObjectName(u"horizontalLayout_125")
        self.horizontalLayout_125.setContentsMargins(0, 0, 0, 0)
        self.label_153 = QLabel(self.GR20)
        self.label_153.setObjectName(u"label_153")
        self.label_153.setMinimumSize(QSize(50, 0))
        self.label_153.setMaximumSize(QSize(50, 16777215))
        self.label_153.setFont(font6)
        self.label_153.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_125.addWidget(self.label_153)

        self.G120 = QLineEdit(self.GR20)
        self.G120.setObjectName(u"G120")
        self.G120.setMinimumSize(QSize(50, 0))
        self.G120.setMaximumSize(QSize(50, 16777215))
        self.G120.setMouseTracking(False)
        self.G120.setStyleSheet(u"")
        self.G120.setAlignment(Qt.AlignCenter)
        self.G120.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_125.addWidget(self.G120)

        self.G220 = QLineEdit(self.GR20)
        self.G220.setObjectName(u"G220")
        self.G220.setMinimumSize(QSize(50, 0))
        self.G220.setMaximumSize(QSize(50, 16777215))
        self.G220.setMouseTracking(False)
        self.G220.setStyleSheet(u"")
        self.G220.setAlignment(Qt.AlignCenter)
        self.G220.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_125.addWidget(self.G220)

        self.G320 = QLineEdit(self.GR20)
        self.G320.setObjectName(u"G320")
        self.G320.setMinimumSize(QSize(50, 0))
        self.G320.setMaximumSize(QSize(50, 16777215))
        self.G320.setMouseTracking(False)
        self.G320.setStyleSheet(u"")
        self.G320.setAlignment(Qt.AlignCenter)
        self.G320.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_125.addWidget(self.G320)


        self.verticalLayout_32.addWidget(self.GR20)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_32.addItem(self.verticalSpacer_7)


        self.horizontalLayout_12.addWidget(self.frame_127)


        self.verticalLayout_16.addWidget(self.frame_21)

        self.frame_68 = QFrame(self.frame_47)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setMaximumSize(QSize(16777215, 80))
        self.frame_68.setFrameShape(QFrame.NoFrame)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.frame_68)
        self.horizontalLayout_53.setSpacing(0)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 10, 0, 0)
        self.nextButtonLiberdade = QPushButton(self.frame_68)
        self.nextButtonLiberdade.setObjectName(u"nextButtonLiberdade")
        self.nextButtonLiberdade.setMinimumSize(QSize(0, 30))
        self.nextButtonLiberdade.setMaximumSize(QSize(150, 16777215))
        self.nextButtonLiberdade.setFont(font4)
        self.nextButtonLiberdade.setStyleSheet(u"QPushButton {\n"
"	padding-left: 5px;\n"
"	background-color: rgb(38, 40, 61);\n"
"	border:none;\n"
"	border-radius:15px;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 3px solid;\n"
"	background-color:rgb(241, 102, 55);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color:rgb(241, 102, 55);\n"
"}\n"
"")

        self.horizontalLayout_53.addWidget(self.nextButtonLiberdade)


        self.verticalLayout_16.addWidget(self.frame_68)


        self.horizontalLayout_54.addWidget(self.frame_47)

        self.stackedWidget.addWidget(self.Liberdade)
        self.graphPage = QWidget()
        self.graphPage.setObjectName(u"graphPage")
        self.horizontalLayout_13 = QHBoxLayout(self.graphPage)
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.frame_33 = QFrame(self.graphPage)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setStyleSheet(u"")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_33)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frame_35 = QFrame(self.frame_33)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)

        self.verticalLayout_25.addWidget(self.frame_35)


        self.horizontalLayout_13.addWidget(self.frame_33)

        self.frame_24 = QFrame(self.graphPage)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(420, 0))
        self.frame_24.setMaximumSize(QSize(420, 16777215))
        self.frame_24.setStyleSheet(u"QFrame{\n"
"	border-radius: 6px;\n"
"background-color: rgb(148, 147, 150);\n"
"}\n"
"")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_25 = QFrame(self.frame_24)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(400, 0))
        self.frame_25.setMaximumSize(QSize(500, 16777215))
        self.frame_25.setStyleSheet(u"QComboBox {\n"
"	border: 1px solid rgb(38, 40, 61);\n"
"	border-radius: 15px;\n"
"	background:  rgb(70, 70, 70);\n"
"	padding: 10x 23px 5px 5x;\n"
"	min-width: 10em;\n"
"	color: rgb(255, 255, 255);\n"
"	margin-left: 5px;\n"
"	margin-right: 5px;\n"
"	padding-left: 8px\n"
"}\n"
"\n"
"QComboBox::disabled{\n"
"	color: rgb(136, 138, 133)\n"
"}\n"
"\n"
"QComboBox::down-arrow:disabled {    \n"
"	image: url(:/icons/img/downArrowDis.png);\n"
"}\n"
"\n"
"QComboBox::hover{\n"
"border: 3px solid  rgb(38, 40, 61);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 20px;\n"
" \n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {    \n"
"	image: url(:/icons/img/downArrow.png);\n"
"	width : 12px;\n"
"}\n"
"\n"
"QComboBox QAbstractView{\n"
"	background-color: #4f4f4f;\n"
"	color: #999999;\n"
" \n"
"	selection-background-color: rgb(70, 70, 70);\n"
"	selection-color: #4f4f4f;\n"
"}\n"
"\n"
"QCheckBox{\n"
""
                        "	color: rgb(255,255,255);\n"
"}\n"
"QCheckBox::indicator{\n"
"	background-color: rgb(70,70,70);\n"
"	color: rgb(241,102,55);\n"
"	border-radius:6px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"	background-color: rgb(241,102,55);\n"
"	border: 2px solid rgb(70,70,70);\n"
"}\n"
"\n"
"QCheckBox:disabled{\n"
" color: rgb(136, 138, 133);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:disabled{\n"
"	background-color: rgb(136, 138, 133);\n"
"}")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_25)
        self.verticalLayout_14.setSpacing(10)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(5, 5, 5, 0)
        self.frame_27 = QFrame(self.frame_25)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMinimumSize(QSize(235, 52))
        self.frame_27.setMaximumSize(QSize(16777215, 52))
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.frame_27)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(50, 50))
        self.label_14.setMaximumSize(QSize(50, 50))
        self.label_14.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(70,70,70);\n"
"	border-radius: 25px;\n"
"}")
        self.label_14.setPixmap(QPixmap(u":/icons/img/settingsEnable.png"))
        self.label_14.setScaledContents(True)
        self.label_14.setMargin(10)

        self.horizontalLayout_14.addWidget(self.label_14)

        self.label_15 = QLabel(self.frame_27)
        self.label_15.setObjectName(u"label_15")
        font7 = QFont()
        font7.setFamilies([u"PF BeauSans Pro"])
        font7.setPointSize(18)
        font7.setBold(True)
        self.label_15.setFont(font7)
        self.label_15.setStyleSheet(u"color: rgb(38, 40, 61);")

        self.horizontalLayout_14.addWidget(self.label_15)


        self.verticalLayout_14.addWidget(self.frame_27)

        self.frame_28 = QFrame(self.frame_25)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMinimumSize(QSize(225, 80))
        self.frame_28.setMaximumSize(QSize(16777215, 16777215))
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_28)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.frame_28)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(16777215, 20))
        font8 = QFont()
        font8.setFamilies([u"PF BeauSans Pro"])
        font8.setPointSize(12)
        font8.setBold(False)
        self.label_16.setFont(font8)
        self.label_16.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_16.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_28.addWidget(self.label_16)

        self.mainBox = QComboBox(self.frame_28)
        self.mainBox.addItem("")
        self.mainBox.setObjectName(u"mainBox")
        self.mainBox.setMinimumSize(QSize(243, 30))
        self.mainBox.setMaximumSize(QSize(16777215, 30))
        font9 = QFont()
        font9.setFamilies([u"PF BeauSans Pro"])
        font9.setPointSize(11)
        self.mainBox.setFont(font9)
        self.mainBox.setStyleSheet(u"")

        self.verticalLayout_28.addWidget(self.mainBox)


        self.verticalLayout_14.addWidget(self.frame_28)

        self.frame_29 = QFrame(self.frame_25)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(225, 80))
        self.frame_29.setMaximumSize(QSize(16777215, 16777215))
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_29)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.frame_29)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(16777215, 20))
        self.label_17.setFont(font8)
        self.label_17.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_17.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_29.addWidget(self.label_17)

        self.domainBox = QComboBox(self.frame_29)
        self.domainBox.addItem("")
        self.domainBox.addItem("")
        self.domainBox.addItem("")
        self.domainBox.addItem("")
        self.domainBox.setObjectName(u"domainBox")
        self.domainBox.setEnabled(True)
        self.domainBox.setMinimumSize(QSize(243, 30))
        self.domainBox.setMaximumSize(QSize(16777215, 30))
        self.domainBox.setFont(font9)
        self.domainBox.setEditable(False)

        self.verticalLayout_29.addWidget(self.domainBox)


        self.verticalLayout_14.addWidget(self.frame_29)

        self.frame_samplingBox = QFrame(self.frame_25)
        self.frame_samplingBox.setObjectName(u"frame_samplingBox")
        self.frame_samplingBox.setMinimumSize(QSize(0, 150))
        self.frame_samplingBox.setMaximumSize(QSize(16777215, 16777215))
        self.frame_samplingBox.setStyleSheet(u"")
        self.frame_samplingBox.setFrameShape(QFrame.StyledPanel)
        self.frame_samplingBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_samplingBox)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 11, 0, 0)
        self.label_18 = QLabel(self.frame_samplingBox)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(16777215, 20))
        self.label_18.setFont(font8)
        self.label_18.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_18.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_34.addWidget(self.label_18)

        self.frame_111 = QFrame(self.frame_samplingBox)
        self.frame_111.setObjectName(u"frame_111")
        self.frame_111.setMinimumSize(QSize(0, 180))
        self.frame_111.setMaximumSize(QSize(16777215, 16777215))
        self.frame_111.setFrameShape(QFrame.StyledPanel)
        self.frame_111.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_111)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_45 = QFrame(self.frame_111)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_45)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(11, 0, 0, 0)
        self.label_25 = QLabel(self.frame_45)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font3)
        self.label_25.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_25.setWordWrap(True)

        self.verticalLayout_37.addWidget(self.label_25)

        self.label_26 = QLabel(self.frame_45)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font9)
        self.label_26.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_26.setWordWrap(True)

        self.verticalLayout_37.addWidget(self.label_26)

        self.label_24 = QLabel(self.frame_45)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font9)
        self.label_24.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_24.setWordWrap(True)

        self.verticalLayout_37.addWidget(self.label_24)


        self.horizontalLayout_21.addWidget(self.frame_45)

        self.frame_31 = QFrame(self.frame_111)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMaximumSize(QSize(120, 16777215))
        self.frame_31.setStyleSheet(u"QLabel {\n"
"	border: 1px solid #333333;\n"
"	border-radius: 15px;\n"
"	background:  rgb(70, 70, 70);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.frame_31.setLineWidth(14)
        self.verticalLayout_36 = QVBoxLayout(self.frame_31)
        self.verticalLayout_36.setSpacing(20)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(11, 0, 5, 0)
        self.label_19 = QLabel(self.frame_31)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(0, 30))
        self.label_19.setMaximumSize(QSize(120, 30))
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_36.addWidget(self.label_19)

        self.label_21 = QLabel(self.frame_31)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(0, 30))
        self.label_21.setMaximumSize(QSize(120, 30))
        self.label_21.setAlignment(Qt.AlignCenter)

        self.verticalLayout_36.addWidget(self.label_21)

        self.label_20 = QLabel(self.frame_31)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(0, 30))
        self.label_20.setMaximumSize(QSize(120, 30))
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_36.addWidget(self.label_20)


        self.horizontalLayout_21.addWidget(self.frame_31)


        self.verticalLayout_34.addWidget(self.frame_111)


        self.verticalLayout_14.addWidget(self.frame_samplingBox)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_2)

        self.frame_30 = QFrame(self.frame_25)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMinimumSize(QSize(225, 100))
        self.frame_30.setMaximumSize(QSize(16777215, 100))
        self.frame_30.setLayoutDirection(Qt.LeftToRight)
        self.frame_30.setStyleSheet(u"")
        self.frame_30.setFrameShape(QFrame.NoFrame)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_20.setSpacing(10)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.exportFig = QPushButton(self.frame_30)
        self.exportFig.setObjectName(u"exportFig")
        self.exportFig.setEnabled(True)
        self.exportFig.setMinimumSize(QSize(130, 30))
        self.exportFig.setMaximumSize(QSize(130, 30))
        font10 = QFont()
        font10.setFamilies([u"PF BeauSans Pro"])
        font10.setPointSize(12)
        self.exportFig.setFont(font10)
        self.exportFig.setStyleSheet(u"QPushButton {\n"
"	padding-left: 5px;\n"
"	background-color: rgb(38, 40, 61);\n"
"	border:none;\n"
"	border-radius:15px;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 3px solid;\n"
"	background-color:rgba(241, 102, 55,150);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color:rgb(241, 102, 55);\n"
"}\n"
"\n"
"")

        self.horizontalLayout_20.addWidget(self.exportFig)

        self.changeData = QPushButton(self.frame_30)
        self.changeData.setObjectName(u"changeData")
        self.changeData.setEnabled(True)
        self.changeData.setMinimumSize(QSize(130, 30))
        self.changeData.setMaximumSize(QSize(130, 30))
        self.changeData.setFont(font10)
        self.changeData.setStyleSheet(u"QPushButton {\n"
"	padding-left: 5px;\n"
"	background-color: rgb(38, 40, 61);\n"
"	border:none;\n"
"	border-radius:15px;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 3px solid;\n"
"	background-color:rgba(241, 102, 55,150);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color:rgb(241, 102, 55);\n"
"}\n"
"\n"
"")

        self.horizontalLayout_20.addWidget(self.changeData)

        self.initialPage = QPushButton(self.frame_30)
        self.initialPage.setObjectName(u"initialPage")
        self.initialPage.setEnabled(True)
        self.initialPage.setMinimumSize(QSize(130, 30))
        self.initialPage.setMaximumSize(QSize(130, 30))
        self.initialPage.setFont(font10)
        self.initialPage.setStyleSheet(u"QPushButton {\n"
"	padding-left: 5px;\n"
"	background-color: rgb(38, 40, 61);\n"
"	border:none;\n"
"	border-radius:15px;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 3px solid;\n"
"	background-color:rgba(241, 102, 55,150);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color:rgb(241, 102, 55);\n"
"}\n"
"\n"
"")

        self.horizontalLayout_20.addWidget(self.initialPage)


        self.verticalLayout_14.addWidget(self.frame_30)


        self.horizontalLayout_17.addWidget(self.frame_25)


        self.horizontalLayout_13.addWidget(self.frame_24)

        self.stackedWidget.addWidget(self.graphPage)
        self.startPage = QWidget()
        self.startPage.setObjectName(u"startPage")
        self.verticalLayout_21 = QVBoxLayout(self.startPage)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame_69 = QFrame(self.startPage)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_69)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.startButton = QPushButton(self.frame_69)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setMinimumSize(QSize(160, 160))
        self.startButton.setMaximumSize(QSize(160, 160))
        font11 = QFont()
        font11.setPointSize(23)
        font11.setBold(True)
        self.startButton.setFont(font11)
        self.startButton.setStyleSheet(u"QPushButton{\n"
"border-radius: 80px;\n"
"background-color: rgb(38, 40, 61);\n"
"color: rgb(255, 255, 255);\n"
"border: 4px solid rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 4px solid;\n"
"	background-color:rgba(241, 102, 55, 200);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color:rgb(241, 102, 55);\n"
"}\n"
"\n"
"\n"
"\n"
"	\n"
"")

        self.horizontalLayout_34.addWidget(self.startButton)


        self.verticalLayout_21.addWidget(self.frame_69)

        self.frame_22 = QFrame(self.startPage)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMaximumSize(QSize(16777215, 75))
        self.frame_22.setLayoutDirection(Qt.LeftToRight)
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(10, 0, 0, 0)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_7)

        self.frame_70 = QFrame(self.frame_22)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_70)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.saveDataRadioButton = QRadioButton(self.frame_70)
        self.saveDataRadioButton.setObjectName(u"saveDataRadioButton")
        self.saveDataRadioButton.setFont(font3)
        self.saveDataRadioButton.setAutoExclusive(False)

        self.verticalLayout_22.addWidget(self.saveDataRadioButton)

        self.sampleDataRadioButton = QRadioButton(self.frame_70)
        self.sampleDataRadioButton.setObjectName(u"sampleDataRadioButton")
        self.sampleDataRadioButton.setFont(font3)
        self.sampleDataRadioButton.setAutoExclusive(False)

        self.verticalLayout_22.addWidget(self.sampleDataRadioButton)


        self.horizontalLayout_23.addWidget(self.frame_70)


        self.verticalLayout_21.addWidget(self.frame_22)

        self.stackedWidget.addWidget(self.startPage)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.Rodape = QFrame(self.centralwidget)
        self.Rodape.setObjectName(u"Rodape")
        self.Rodape.setMinimumSize(QSize(0, 60))
        self.Rodape.setMaximumSize(QSize(16777215, 60))
        self.Rodape.setStyleSheet(u"background-color: rgb(38, 40, 61);")
        self.Rodape.setFrameShape(QFrame.StyledPanel)
        self.Rodape.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.Rodape)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.label_9 = QLabel(self.Rodape)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color: rgb(214, 214, 214);")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_9)


        self.verticalLayout.addWidget(self.Rodape)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Applied Solid Mechanics", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">Beam Analysis Software</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"PROBLEM DATA", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Number of elements:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Number of nodes:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Number of degress of freedom:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Applied load (N):", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Force application node:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Element thickness (mm):", None))
        self.h.setInputMask("")
        self.h.setText("")
        self.h.setPlaceholderText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Application direction:", None))
        self.dir_P.setInputMask("")
        self.dir_P.setText("")
        self.dir_P.setPlaceholderText(QCoreApplication.translate("MainWindow", u"x, y ou z", None))
        self.nextButtonInitial.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"NODAL COORDINATES", None))
        self.label_123.setText(QCoreApplication.translate("MainWindow", u"Node", None))
        self.label_124.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_125.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"Node", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"11", None))
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"13", None))
        self.label_116.setText(QCoreApplication.translate("MainWindow", u"14", None))
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"16", None))
        self.label_119.setText(QCoreApplication.translate("MainWindow", u"17", None))
        self.label_120.setText(QCoreApplication.translate("MainWindow", u"18", None))
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"19", None))
        self.label_122.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.nextButtonNo.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"NODAL INCIDENCES", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Element", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Node 1", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Node 2", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"11", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"13", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"14", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"16", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"17", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"18", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"19", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Element", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Node 1", None))
        self.label_139.setText(QCoreApplication.translate("MainWindow", u"Node 2", None))
        self.label_161.setText(QCoreApplication.translate("MainWindow", u"21", None))
        self.label_163.setText(QCoreApplication.translate("MainWindow", u"22", None))
        self.label_175.setText(QCoreApplication.translate("MainWindow", u"23", None))
        self.label_166.setText(QCoreApplication.translate("MainWindow", u"24", None))
        self.label_171.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.label_177.setText(QCoreApplication.translate("MainWindow", u"26", None))
        self.label_159.setText(QCoreApplication.translate("MainWindow", u"27", None))
        self.label_167.setText(QCoreApplication.translate("MainWindow", u"28", None))
        self.label_168.setText(QCoreApplication.translate("MainWindow", u"29", None))
        self.label_176.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.label_173.setText(QCoreApplication.translate("MainWindow", u"31", None))
        self.label_178.setText(QCoreApplication.translate("MainWindow", u"32", None))
        self.label_160.setText(QCoreApplication.translate("MainWindow", u"33", None))
        self.label_169.setText(QCoreApplication.translate("MainWindow", u"34", None))
        self.label_174.setText(QCoreApplication.translate("MainWindow", u"35", None))
        self.label_162.setText(QCoreApplication.translate("MainWindow", u"36", None))
        self.label_172.setText(QCoreApplication.translate("MainWindow", u"37", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"38", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"39", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"40", None))
        self.nextButtonIncidencias.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"DEGREES OF FREEDOM", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Node", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"u", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"v", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"theta", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_140.setText(QCoreApplication.translate("MainWindow", u"Node", None))
        self.label_141.setText(QCoreApplication.translate("MainWindow", u"u", None))
        self.label_142.setText(QCoreApplication.translate("MainWindow", u"v", None))
        self.label_143.setText(QCoreApplication.translate("MainWindow", u"theta", None))
        self.label_144.setText(QCoreApplication.translate("MainWindow", u"11", None))
        self.label_145.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.label_146.setText(QCoreApplication.translate("MainWindow", u"13", None))
        self.label_147.setText(QCoreApplication.translate("MainWindow", u"14", None))
        self.label_148.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.label_149.setText(QCoreApplication.translate("MainWindow", u"16", None))
        self.label_150.setText(QCoreApplication.translate("MainWindow", u"17", None))
        self.label_151.setText(QCoreApplication.translate("MainWindow", u"18", None))
        self.label_152.setText(QCoreApplication.translate("MainWindow", u"19", None))
        self.label_153.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.nextButtonLiberdade.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_14.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Element:", None))
        self.mainBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Full structure", None))

        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Domain:", None))
        self.domainBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Normal Stress", None))
        self.domainBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Shear Stress", None))
        self.domainBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Moment", None))
        self.domainBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Von Mises", None))

        self.domainBox.setCurrentText(QCoreApplication.translate("MainWindow", u"Normal Stress", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Data:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Maximum displacement magnitude", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Max. von Mises Stress in the Element", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Max. von Mises Stress in the Structure", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.exportFig.setText(QCoreApplication.translate("MainWindow", u"Export figure", None))
        self.changeData.setText(QCoreApplication.translate("MainWindow", u"Change datas", None))
        self.initialPage.setText(QCoreApplication.translate("MainWindow", u"Initial page", None))
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.saveDataRadioButton.setText(QCoreApplication.translate("MainWindow", u"Save Data", None))
        self.sampleDataRadioButton.setText(QCoreApplication.translate("MainWindow", u"Use sample data.", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Developed by  Juc\u00e9lio Tavares Junior and Marcelo Krajnc", None))
    # retranslateUi

