# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\charl\source\repos\crgrove\automated-drone-image-analysis-tool\resources/views/algorithms/MatchedFilter.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MatchedFilter(object):
    def setupUi(self, MatchedFilter):
        MatchedFilter.setObjectName("MatchedFilter")
        MatchedFilter.resize(674, 94)
        self.verticalLayout = QtWidgets.QVBoxLayout(MatchedFilter)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ColorSelectionLayout = QtWidgets.QHBoxLayout()
        self.ColorSelectionLayout.setObjectName("ColorSelectionLayout")
        self.colorButton = QtWidgets.QPushButton(MatchedFilter)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/color.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.colorButton.setIcon(icon)
        self.colorButton.setObjectName("colorButton")
        self.ColorSelectionLayout.addWidget(self.colorButton)
        self.colorSample = QtWidgets.QFrame(MatchedFilter)
        self.colorSample.setMinimumSize(QtCore.QSize(50, 20))
        self.colorSample.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.colorSample.setFrameShadow(QtWidgets.QFrame.Raised)
        self.colorSample.setObjectName("colorSample")
        self.ColorSelectionLayout.addWidget(self.colorSample)
        self.SilderLayout = QtWidgets.QHBoxLayout()
        self.SilderLayout.setObjectName("SilderLayout")
        self.thresholdLabel = QtWidgets.QLabel(MatchedFilter)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.thresholdLabel.setFont(font)
        self.thresholdLabel.setObjectName("thresholdLabel")
        self.SilderLayout.addWidget(self.thresholdLabel)
        self.thresholdSlider = QtWidgets.QSlider(MatchedFilter)
        self.thresholdSlider.setMinimum(1)
        self.thresholdSlider.setMaximum(10)
        self.thresholdSlider.setPageStep(1)
        self.thresholdSlider.setProperty("value", 3)
        self.thresholdSlider.setOrientation(QtCore.Qt.Horizontal)
        self.thresholdSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.thresholdSlider.setTickInterval(0)
        self.thresholdSlider.setObjectName("thresholdSlider")
        self.SilderLayout.addWidget(self.thresholdSlider)
        self.thresholdValueLabel = QtWidgets.QLabel(MatchedFilter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.thresholdValueLabel.setFont(font)
        self.thresholdValueLabel.setObjectName("thresholdValueLabel")
        self.SilderLayout.addWidget(self.thresholdValueLabel)
        self.ColorSelectionLayout.addLayout(self.SilderLayout)
        self.verticalLayout.addLayout(self.ColorSelectionLayout)

        self.retranslateUi(MatchedFilter)
        QtCore.QMetaObject.connectSlotsByName(MatchedFilter)

    def retranslateUi(self, MatchedFilter):
        _translate = QtCore.QCoreApplication.translate
        MatchedFilter.setWindowTitle(_translate("MatchedFilter", "Form"))
        self.colorButton.setText(_translate("MatchedFilter", " Pick Color"))
        self.thresholdLabel.setText(_translate("MatchedFilter", "Threshold:"))
        self.thresholdValueLabel.setText(_translate("MatchedFilter", ".3"))
from . import MatchedFilter_rc