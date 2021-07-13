# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewer.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_viewer(object):
    def setupUi(self, viewer):
        viewer.setObjectName("viewer")
        viewer.resize(520, 850)
        self.table = QtWidgets.QTableWidget(viewer)
        self.table.setGeometry(QtCore.QRect(0, 0, 510, 530))
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.label = QtWidgets.QLabel(viewer)
        self.label.setGeometry(QtCore.QRect(10, 570, 59, 15))
        self.label.setObjectName("label")
        self.title = QtWidgets.QPlainTextEdit(viewer)
        self.title.setGeometry(QtCore.QRect(80, 550, 431, 50))
        self.title.setReadOnly(True)
        self.title.setPlainText("")
        self.title.setObjectName("title")
        self.label_2 = QtWidgets.QLabel(viewer)
        self.label_2.setGeometry(QtCore.QRect(10, 630, 59, 15))
        self.label_2.setObjectName("label_2")
        self.link = QtWidgets.QPlainTextEdit(viewer)
        self.link.setGeometry(QtCore.QRect(80, 610, 431, 50))
        self.link.setReadOnly(True)
        self.link.setPlainText("")
        self.link.setObjectName("link")
        self.label_3 = QtWidgets.QLabel(viewer)
        self.label_3.setGeometry(QtCore.QRect(10, 720, 59, 15))
        self.label_3.setObjectName("label_3")
        self.snippet = QtWidgets.QPlainTextEdit(viewer)
        self.snippet.setGeometry(QtCore.QRect(80, 670, 431, 120))
        self.snippet.setReadOnly(True)
        self.snippet.setPlainText("")
        self.snippet.setObjectName("snippet")
        self.label_4 = QtWidgets.QLabel(viewer)
        self.label_4.setGeometry(QtCore.QRect(10, 810, 59, 15))
        self.label_4.setObjectName("label_4")
        self.citation = QtWidgets.QLineEdit(viewer)
        self.citation.setGeometry(QtCore.QRect(80, 810, 113, 23))
        self.citation.setText("")
        self.citation.setReadOnly(True)
        self.citation.setObjectName("citation")
        self.pbLoad = QtWidgets.QPushButton(viewer)
        self.pbLoad.setGeometry(QtCore.QRect(330, 810, 80, 23))
        self.pbLoad.setObjectName("pbLoad")
        self.pbClose = QtWidgets.QPushButton(viewer)
        self.pbClose.setGeometry(QtCore.QRect(430, 810, 80, 23))
        self.pbClose.setObjectName("pbClose")

        self.retranslateUi(viewer)
        self.pbClose.clicked.connect(viewer.close)
        QtCore.QMetaObject.connectSlotsByName(viewer)

    def retranslateUi(self, viewer):
        _translate = QtCore.QCoreApplication.translate
        viewer.setWindowTitle(_translate("viewer", "Table Viewer"))
        self.label.setText(_translate("viewer", "Title:"))
        self.label_2.setText(_translate("viewer", "Link:"))
        self.label_3.setText(_translate("viewer", "Snippet:"))
        self.label_4.setText(_translate("viewer", "#Citation:"))
        self.pbLoad.setText(_translate("viewer", "Load"))
        self.pbClose.setText(_translate("viewer", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    viewer = QtWidgets.QWidget()
    ui = Ui_viewer()
    ui.setupUi(viewer)
    viewer.show()
    sys.exit(app.exec_())

