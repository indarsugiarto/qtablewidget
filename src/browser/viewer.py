from PyQt5 import QtWidgets, QtGui
from .viewer_ui import Ui_viewer
import pandas as pd

class viewer(QtWidgets.QWidget, Ui_viewer):
    def __init__(self, parent=None):
        super(viewer,self).__init__(parent)
        self.setupUi(self)
        self.pbLoad.clicked.connect(self.loadFile)
        self.table.itemSelectionChanged.connect(self.showDetail)
        self.resizeEvent = self.onResize
        self.df = None

    def onResize(self, event: QtGui.QResizeEvent):
        super().resizeEvent(event)
        self.table.setGeometry(0,0,self.width()-10,530)
        self.title.setGeometry(80,550,self.width()-90,50)
        self.link.setGeometry(80,610,self.width()-90,50)
        self.snippet.setGeometry(80,670,self.width()-90,120)

    def showDetail(self):
        if self.df is None:
            return
        ttl = self.df.iloc[self.table.currentRow()]['title']
        lnk = self.df.iloc[self.table.currentRow()]['link']
        snp = self.df.iloc[self.table.currentRow()]['snippet']
        cit = str(self.df.iloc[self.table.currentRow()]['cited'])
        self.title.setPlainText(ttl)
        self.link.setPlainText(lnk)
        self.snippet.setPlainText(snp)
        self.citation.setText(cit)

    def loadFile(self):
        fname,_ = QtWidgets.QFileDialog.getOpenFileName(self,"Load File","","Data File (*.csv)")
        #fname akan lengkap beserta path-nya
        if fname:
            print("Loading",fname)
            self.df = pd.read_csv(fname,header=0)
            if len(self.df) > 0:
                self.table.clear()
                self.table.setColumnCount(len(self.df.columns))
                self.table.setRowCount(len(self.df))
                c = list(self.df.columns)
                self.table.setHorizontalHeaderLabels(c)
                r = [str(i) for i in range(1,len(self.df)+1)]
                self.table.setVerticalHeaderLabels(r)
                for i in range(len(self.df)):
                    for j in range(len(c)):
                        item = QtWidgets.QTableWidgetItem()
                        self.table.setItem(i, j, item)

                        txt = str(self.df.iloc[i][c[j]])
                        item = self.table.item(i,j)
                        item.setText(txt)

