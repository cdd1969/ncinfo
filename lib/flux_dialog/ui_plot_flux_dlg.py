# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '\\Widar\home\ak2stud\Nick\python_scripts\dev\nc_info_gui\wrk\lib\flux_dialog\plot_flux_dlg.ui'
#
# Created: Wed Aug 12 14:35:37 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(704, 571)
        Dialog.setMinimumSize(QtCore.QSize(350, 450))
        Dialog.setModal(True)
        self.gridLayout_5 = QtGui.QGridLayout(Dialog)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setMinimumSize(QtCore.QSize(300, 200))
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox_p1 = QtGui.QGroupBox(Dialog)
        self.groupBox_p1.setMinimumSize(QtCore.QSize(200, 70))
        self.groupBox_p1.setObjectName(_fromUtf8("groupBox_p1"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_p1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.groupBox_p1)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_j1 = QtGui.QLineEdit(self.groupBox_p1)
        self.lineEdit_j1.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEdit_j1.setText(_fromUtf8(""))
        self.lineEdit_j1.setObjectName(_fromUtf8("lineEdit_j1"))
        self.gridLayout.addWidget(self.lineEdit_j1, 0, 3, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_p1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.lineEdit_i1 = QtGui.QLineEdit(self.groupBox_p1)
        self.lineEdit_i1.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEdit_i1.setObjectName(_fromUtf8("lineEdit_i1"))
        self.gridLayout.addWidget(self.lineEdit_i1, 0, 1, 1, 1)
        self.pushButton_pick1 = QtGui.QPushButton(self.groupBox_p1)
        self.pushButton_pick1.setMinimumSize(QtCore.QSize(30, 0))
        self.pushButton_pick1.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_pick1.setObjectName(_fromUtf8("pushButton_pick1"))
        self.gridLayout.addWidget(self.pushButton_pick1, 0, 4, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_p1)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setMinimumSize(QtCore.QSize(200, 70))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.lineEdit_i2 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_i2.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEdit_i2.setObjectName(_fromUtf8("lineEdit_i2"))
        self.gridLayout_2.addWidget(self.lineEdit_i2, 0, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 0, 2, 1, 1)
        self.lineEdit_j2 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_j2.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEdit_j2.setText(_fromUtf8(""))
        self.lineEdit_j2.setObjectName(_fromUtf8("lineEdit_j2"))
        self.gridLayout_2.addWidget(self.lineEdit_j2, 0, 3, 1, 1)
        self.pushButton_pick2 = QtGui.QPushButton(self.groupBox)
        self.pushButton_pick2.setMinimumSize(QtCore.QSize(30, 0))
        self.pushButton_pick2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_pick2.setObjectName(_fromUtf8("pushButton_pick2"))
        self.gridLayout_2.addWidget(self.pushButton_pick2, 0, 4, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.groupBox_4 = QtGui.QGroupBox(Dialog)
        self.groupBox_4.setMinimumSize(QtCore.QSize(300, 130))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.lineEdit_bathymetry = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_bathymetry.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEdit_bathymetry.setObjectName(_fromUtf8("lineEdit_bathymetry"))
        self.gridLayout_3.addWidget(self.lineEdit_bathymetry, 3, 0, 1, 1)
        self.label_latVar = QtGui.QLabel(self.groupBox_4)
        self.label_latVar.setObjectName(_fromUtf8("label_latVar"))
        self.gridLayout_3.addWidget(self.label_latVar, 1, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox_4)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)
        self.pushButton_selectBathymetry = QtGui.QPushButton(self.groupBox_4)
        self.pushButton_selectBathymetry.setMinimumSize(QtCore.QSize(50, 20))
        self.pushButton_selectBathymetry.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_selectBathymetry.setObjectName(_fromUtf8("pushButton_selectBathymetry"))
        self.gridLayout_3.addWidget(self.pushButton_selectBathymetry, 3, 1, 1, 1)
        self.label_lonVar = QtGui.QLabel(self.groupBox_4)
        self.label_lonVar.setObjectName(_fromUtf8("label_lonVar"))
        self.gridLayout_3.addWidget(self.label_lonVar, 2, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox_4)
        self.gridLayout_5.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setMinimumSize(QtCore.QSize(300, 160))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_10 = QtGui.QLabel(self.groupBox_2)
        self.label_10.setMinimumSize(QtCore.QSize(100, 0))
        self.label_10.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_4.addWidget(self.label_10, 0, 0, 1, 1)
        self.comboBox_velx = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_velx.setMinimumSize(QtCore.QSize(0, 20))
        self.comboBox_velx.setObjectName(_fromUtf8("comboBox_velx"))
        self.gridLayout_4.addWidget(self.comboBox_velx, 2, 1, 1, 1)
        self.comboBox_vely = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_vely.setMinimumSize(QtCore.QSize(0, 20))
        self.comboBox_vely.setObjectName(_fromUtf8("comboBox_vely"))
        self.gridLayout_4.addWidget(self.comboBox_vely, 3, 1, 1, 1)
        self.comboBox_spm = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_spm.setMinimumSize(QtCore.QSize(0, 20))
        self.comboBox_spm.setObjectName(_fromUtf8("comboBox_spm"))
        self.gridLayout_4.addWidget(self.comboBox_spm, 4, 1, 1, 1)
        self.comboBox_waterDepth = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_waterDepth.setMinimumSize(QtCore.QSize(0, 20))
        self.comboBox_waterDepth.setObjectName(_fromUtf8("comboBox_waterDepth"))
        self.gridLayout_4.addWidget(self.comboBox_waterDepth, 0, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.groupBox_2)
        self.label_9.setMinimumSize(QtCore.QSize(100, 0))
        self.label_9.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_4.addWidget(self.label_9, 2, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox_2)
        self.label_8.setMinimumSize(QtCore.QSize(100, 0))
        self.label_8.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_4.addWidget(self.label_8, 3, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setMinimumSize(QtCore.QSize(100, 0))
        self.label_7.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_4.addWidget(self.label_7, 4, 0, 1, 1)
        self.comboBox_relativeLayerThickness = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_relativeLayerThickness.setObjectName(_fromUtf8("comboBox_relativeLayerThickness"))
        self.gridLayout_4.addWidget(self.comboBox_relativeLayerThickness, 1, 1, 1, 1)
        self.label_11 = QtGui.QLabel(self.groupBox_2)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_4.addWidget(self.label_11, 1, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_2, 2, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_5.addWidget(self.buttonBox, 3, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Plot mass flux through section", None))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p>Script will calculate mass-flux for a given 2D section (user defined x-y-line, all depth-layers) according to following equation:</p><p align=\"center\"><span style=\" font-weight:600;\">mass_flux = length*thickness*normal_velocity*spm</span></p><p>Note: (1) all calculations are done cell-wise. (2) normal_velocity is a magnitude of velocity vector which is normal to current section line</p><p>If you are interested in the basic steps of this script, you can read information below. This script will make a 2D crossection passing through all depth layers (z-index). Section line can be either horzontal or vertical and passes always through cell-centers. Line is specified through piking two points (i-, j- indexes of two cells). Script will calculate arc-length of each cell based on <a href=\"http://pydoc.net/Python/obspy.core/0.7.1/obspy.core.util.geodetics/\"><span style=\" text-decoration: underline; color:#0000ff;\">Vincenty solution for ellipsoid</span></a>. Note that the change of the Earth radius with depth is ignored, meaning that all cells for specific [i, j] regardless [z] will have equal arc_length. For this calculation you should provide LAT/LON info in section &quot;Grid Info&quot;. Afterwards , layer thickness is calculated based on layer_height (elevation of the layer bottom + layer top of the very top cell)<br/></p></body></html>", None))
        self.groupBox_p1.setTitle(_translate("Dialog", "Point 1", None))
        self.label.setText(_translate("Dialog", "cell [i]", None))
        self.label_2.setText(_translate("Dialog", "cell [j]", None))
        self.pushButton_pick1.setText(_translate("Dialog", "Pick", None))
        self.groupBox.setTitle(_translate("Dialog", "Point 2", None))
        self.label_4.setText(_translate("Dialog", "cell [i]", None))
        self.label_5.setText(_translate("Dialog", "cell [j]", None))
        self.pushButton_pick2.setText(_translate("Dialog", "Pick", None))
        self.groupBox_4.setTitle(_translate("Dialog", "Grid info", None))
        self.lineEdit_bathymetry.setText(_translate("Dialog", "Select the netCDF file with LAT/LON information...", None))
        self.label_latVar.setText(_translate("Dialog", "Lat variable = ?", None))
        self.label_6.setText(_translate("Dialog", "cell size (lat, lon) = (?, ?)", None))
        self.pushButton_selectBathymetry.setText(_translate("Dialog", "Select", None))
        self.label_lonVar.setText(_translate("Dialog", "Lon variable = ?", None))
        self.groupBox_2.setTitle(_translate("Dialog", "Variables...", None))
        self.label_10.setText(_translate("Dialog", "Water depth", None))
        self.label_9.setText(_translate("Dialog", "Velocity X var", None))
        self.label_8.setText(_translate("Dialog", "Velocity Y var", None))
        self.label_7.setText(_translate("Dialog", "SPM var", None))
        self.label_11.setText(_translate("Dialog", "Relative Layer Thickness", None))
