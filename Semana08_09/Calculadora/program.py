import sys
from PySide2 import QtCore, QtGui, QtWidgets
from Calculadora import Ui_Calculadora

class MainWindow(QtWidgets.QMainWindow, Ui_Calculadora):
    arm = ''
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        
        def calc(arg):
            self.arm = '{}{}'.format(self.arm,arg)
            self.lineEdit.setText('{}'.format(self.arm))
            
        def resolve():
            self.arm = '{}'.format(eval(self.arm))
            self.lineEdit.setText('{}'.format(self.arm))
            
        def apaga():
            self.arm = '0'
            self.lineEdit.setText('{}'.format(self.arm))
            
        def desliga():
            self.arm = ''
            self.lineEdit.setText('{}'.format(self.arm))

        self.p0.clicked.connect(lambda: calc(self.p0.text()))
        self.p1.clicked.connect(lambda: calc(self.p1.text()))
        self.p2.clicked.connect(lambda: calc(self.p2.text()))
        self.p3.clicked.connect(lambda: calc(self.p3.text()))
        self.p4.clicked.connect(lambda: calc(self.p4.text()))
        self.p5.clicked.connect(lambda: calc(self.p5.text()))
        self.p6.clicked.connect(lambda: calc(self.p6.text()))
        self.p7.clicked.connect(lambda: calc(self.p7.text()))
        self.p8.clicked.connect(lambda: calc(self.p8.text()))
        self.p9.clicked.connect(lambda: calc(self.p9.text()))
        self.padi.clicked.connect(lambda: calc(self.padi.text()))
        self.psub.clicked.connect(lambda: calc(self.psub.text()))
        self.pdiv.clicked.connect(lambda: calc(self.pdiv.text()))
        self.pvezes.clicked.connect(lambda: calc(self.pvezes.text()))
        self.once.clicked.connect(lambda: apaga())
        self.off.clicked.connect(lambda: desliga())
        self.pponto.clicked.connect(lambda: calc(self.pponto.text()))
        self.pigual.clicked.connect(lambda: resolve())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
