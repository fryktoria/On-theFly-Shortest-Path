# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DlgLayerSelection.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


#from PyQt5 import QtCore, QtGui, QtWidgets
from qgis.PyQt import QtCore, QtGui, QtWidgets

class Ui_layersDialog(object):
    def setupUi(self, layersDialog):
        layersDialog.setObjectName("layersDialog")
        layersDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        layersDialog.resize(685, 573)
        self.gridLayout_2 = QtWidgets.QGridLayout(layersDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(layersDialog)
        self.tabWidget.setLocale(QtCore.QLocale(QtCore.QLocale.C, QtCore.QLocale.AnyCountry))
        self.tabWidget.setObjectName("tabWidget")
        self.lineLayerTab = QtWidgets.QWidget()
        self.lineLayerTab.setObjectName("lineLayerTab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.lineLayerTab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.lineLayerTab)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineLayerListWidget = QtWidgets.QListWidget(self.lineLayerTab)
        self.lineLayerListWidget.setAlternatingRowColors(False)
        self.lineLayerListWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.lineLayerListWidget.setIconSize(QtCore.QSize(24, 24))
        self.lineLayerListWidget.setTextElideMode(QtCore.Qt.ElideLeft)
        self.lineLayerListWidget.setResizeMode(QtWidgets.QListView.Adjust)
        self.lineLayerListWidget.setSelectionRectVisible(True)
        self.lineLayerListWidget.setObjectName("lineLayerListWidget")
        self.verticalLayout.addWidget(self.lineLayerListWidget)
        self.tabWidget.addTab(self.lineLayerTab, "")
        self.pointLayerTab = QtWidgets.QWidget()
        self.pointLayerTab.setObjectName("pointLayerTab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.pointLayerTab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_2 = QtWidgets.QLabel(self.pointLayerTab)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.pointLayerListWidget = QtWidgets.QListWidget(self.pointLayerTab)
        self.pointLayerListWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.pointLayerListWidget.setObjectName("pointLayerListWidget")
        self.gridLayout_4.addWidget(self.pointLayerListWidget, 1, 0, 1, 1)
        self.tabWidget.addTab(self.pointLayerTab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(layersDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(layersDialog)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(layersDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(layersDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(layersDialog)

    def retranslateUi(self, layersDialog):
        _translate = QtCore.QCoreApplication.translate
        layersDialog.setWindowTitle(_translate("layersDialog", "Layer selection"))
        self.label.setText(_translate("layersDialog", "Select one or more layers to use as path"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.lineLayerTab), _translate("layersDialog", "Line layers"))
        self.label_2.setText(_translate("layersDialog", "Select one or more point layers to use as bridges between line layers"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pointLayerTab), _translate("layersDialog", "Point layers"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    layersDialog = QtWidgets.QDialog()
    ui = Ui_layersDialog()
    ui.setupUi(layersDialog)
    layersDialog.show()
    sys.exit(app.exec_())