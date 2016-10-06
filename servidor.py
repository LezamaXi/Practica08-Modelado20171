import sys
from PyQt4 import QtGui, uic

class MyWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('snake.ui', self)
        self.columnas()
        self.show()

    def columnas(self):
    	self.Tabla.horizontalHeader().setStretchLastSection(True)
    	self.Tabla.verticalHeader().setStretchLastSection(True)
    	self.Tabla.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
    	self.Tabla.verticalHeader().setResizeMode(QtGui.QHeaderView.Stretch)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())