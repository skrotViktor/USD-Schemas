# Form implementation generated from reading ui file 'box.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from pxr.Usdviewq.qt import QtCore, QtGui, QtWidgets
from pxr.Usdviewq import primTreeWidget

def launchDialog(usdviewApi):
    # prim = usdviewApi.stage.GetPrimAtPath("/World/grid/Grid")
    # attr = prim.GetAttribute("warp:sourceFile")
    # _preferencesDlg = Preferences(usdviewApi.qMainWindow, attr)
    dial = Dialog(usdviewApi.qMainWindow, usdviewApi)
    dial.show()
    # _preferencesDlg = None


class Dialog(QtWidgets.QDialog):
    def __init__(self, parent, api):
        super().__init__(parent)
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.addButton = QtWidgets.QPushButton("Add CodeProcAPI to selected", parent=self)
        self.verticalLayout.addWidget(self.addButton)

        self.inputTable = QtWidgets.QTableWidget(parent=self)
        

        self.textEdit = QtWidgets.QTextEdit(parent=self)
        self.textEdit.setMinimumSize(QtCore.QSize(309, 0))
        self.verticalLayout.addWidget(self.textEdit)

        self.pushButton = QtWidgets.QPushButton("PRESS ME", parent=self)
        self.verticalLayout.addWidget(self.pushButton)
