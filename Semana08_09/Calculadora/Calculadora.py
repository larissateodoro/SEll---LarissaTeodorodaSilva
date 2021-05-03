# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Calculadora.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resource_rc

class Ui_Calculadora(object):
    def setupUi(self, Calculadora):
        if not Calculadora.objectName():
            Calculadora.setObjectName(u"Calculadora")
        Calculadora.resize(340, 190)
        Calculadora.setMinimumSize(QSize(340, 190))
        Calculadora.setMaximumSize(QSize(340, 190))
        icon = QIcon()
        icon.addFile(u":/newPrefix/Calculator-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        Calculadora.setWindowIcon(icon)
        self.centralwidget = QWidget(Calculadora)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(85, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.p6 = QPushButton(self.frame)
        self.p6.setObjectName(u"p6")

        self.gridLayout_2.addWidget(self.p6, 3, 1, 1, 1)

        self.once = QPushButton(self.frame)
        self.once.setObjectName(u"once")

        self.gridLayout_2.addWidget(self.once, 0, 0, 1, 2)

        self.p2 = QPushButton(self.frame)
        self.p2.setObjectName(u"p2")

        self.gridLayout_2.addWidget(self.p2, 2, 1, 1, 1)

        self.p8 = QPushButton(self.frame)
        self.p8.setObjectName(u"p8")

        self.gridLayout_2.addWidget(self.p8, 3, 3, 1, 1)

        self.p1 = QPushButton(self.frame)
        self.p1.setObjectName(u"p1")

        self.gridLayout_2.addWidget(self.p1, 2, 0, 1, 1)

        self.psub = QPushButton(self.frame)
        self.psub.setObjectName(u"psub")

        self.gridLayout_2.addWidget(self.psub, 1, 2, 1, 1)

        self.off = QPushButton(self.frame)
        self.off.setObjectName(u"off")

        self.gridLayout_2.addWidget(self.off, 0, 2, 1, 2)

        self.pigual = QPushButton(self.frame)
        self.pigual.setObjectName(u"pigual")

        self.gridLayout_2.addWidget(self.pigual, 4, 3, 1, 1)

        self.p0 = QPushButton(self.frame)
        self.p0.setObjectName(u"p0")

        self.gridLayout_2.addWidget(self.p0, 4, 1, 1, 1)

        self.p5 = QPushButton(self.frame)
        self.p5.setObjectName(u"p5")

        self.gridLayout_2.addWidget(self.p5, 3, 0, 1, 1)

        self.p3 = QPushButton(self.frame)
        self.p3.setObjectName(u"p3")

        self.gridLayout_2.addWidget(self.p3, 2, 2, 1, 1)

        self.pvezes = QPushButton(self.frame)
        self.pvezes.setObjectName(u"pvezes")

        self.gridLayout_2.addWidget(self.pvezes, 1, 1, 1, 1)

        self.padi = QPushButton(self.frame)
        self.padi.setObjectName(u"padi")

        self.gridLayout_2.addWidget(self.padi, 1, 0, 1, 1)

        self.pponto = QPushButton(self.frame)
        self.pponto.setObjectName(u"pponto")

        self.gridLayout_2.addWidget(self.pponto, 4, 2, 1, 1)

        self.p4 = QPushButton(self.frame)
        self.p4.setObjectName(u"p4")

        self.gridLayout_2.addWidget(self.p4, 2, 3, 1, 1)

        self.p7 = QPushButton(self.frame)
        self.p7.setObjectName(u"p7")

        self.gridLayout_2.addWidget(self.p7, 3, 2, 1, 1)

        self.pdiv = QPushButton(self.frame)
        self.pdiv.setObjectName(u"pdiv")

        self.gridLayout_2.addWidget(self.pdiv, 1, 3, 1, 1)

        self.p9 = QPushButton(self.frame)
        self.p9.setObjectName(u"p9")

        self.gridLayout_2.addWidget(self.p9, 4, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 1, 1, 1)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_3.addWidget(self.lineEdit, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        Calculadora.setCentralWidget(self.centralwidget)

        self.retranslateUi(Calculadora)

        QMetaObject.connectSlotsByName(Calculadora)
    # setupUi

    def retranslateUi(self, Calculadora):
        Calculadora.setWindowTitle(QCoreApplication.translate("Calculadora", u"Calculadora", None))
        self.p6.setText(QCoreApplication.translate("Calculadora", u"6", None))
        self.once.setText(QCoreApplication.translate("Calculadora", u"ON/CE", None))
        self.p2.setText(QCoreApplication.translate("Calculadora", u"2", None))
        self.p8.setText(QCoreApplication.translate("Calculadora", u"8", None))
        self.p1.setText(QCoreApplication.translate("Calculadora", u"1", None))
        self.psub.setText(QCoreApplication.translate("Calculadora", u"-", None))
        self.off.setText(QCoreApplication.translate("Calculadora", u"OFF", None))
        self.pigual.setText(QCoreApplication.translate("Calculadora", u"=", None))
        self.p0.setText(QCoreApplication.translate("Calculadora", u"0", None))
        self.p5.setText(QCoreApplication.translate("Calculadora", u"5", None))
        self.p3.setText(QCoreApplication.translate("Calculadora", u"3", None))
        self.pvezes.setText(QCoreApplication.translate("Calculadora", u"*", None))
        self.padi.setText(QCoreApplication.translate("Calculadora", u"+", None))
        self.pponto.setText(QCoreApplication.translate("Calculadora", u".", None))
        self.p4.setText(QCoreApplication.translate("Calculadora", u"4", None))
        self.p7.setText(QCoreApplication.translate("Calculadora", u"7", None))
        self.pdiv.setText(QCoreApplication.translate("Calculadora", u"/", None))
        self.p9.setText(QCoreApplication.translate("Calculadora", u"9", None))
    # retranslateUi

