import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from browser.viewer import viewer

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myViewer = viewer()
    myViewer.show()
    sys.exit(app.exec_())

