# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\charl\source\repos\crgrove\automated-drone-image-analysis-tool\resources/views/algorithms/RXAnomaly.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RXAnomaly(object):
    def setupUi(self, RXAnomaly):
        RXAnomaly.setObjectName("RXAnomaly")
        RXAnomaly.resize(674, 94)
        self.verticalLayout = QtWidgets.QVBoxLayout(RXAnomaly)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.thresholdLabel = QtWidgets.QLabel(RXAnomaly)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.thresholdLabel.setFont(font)
        self.thresholdLabel.setObjectName("thresholdLabel")
        self.horizontalLayout_3.addWidget(self.thresholdLabel)
        self.thresholdSlider = QtWidgets.QSlider(RXAnomaly)
        self.thresholdSlider.setMaximum(1000)
        self.thresholdSlider.setSliderPosition(999)
        self.thresholdSlider.setOrientation(QtCore.Qt.Horizontal)
        self.thresholdSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.thresholdSlider.setObjectName("thresholdSlider")
        self.horizontalLayout_3.addWidget(self.thresholdSlider)
        self.thresholdValueLabel = QtWidgets.QLabel(RXAnomaly)
        self.thresholdValueLabel.setMinimumSize(QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.thresholdValueLabel.setFont(font)
        self.thresholdValueLabel.setObjectName("thresholdValueLabel")
        self.horizontalLayout_3.addWidget(self.thresholdValueLabel)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(RXAnomaly)
        QtCore.QMetaObject.connectSlotsByName(RXAnomaly)

    def retranslateUi(self, RXAnomaly):
        _translate = QtCore.QCoreApplication.translate
        RXAnomaly.setWindowTitle(_translate("RXAnomaly", "Form"))
        self.thresholdLabel.setText(_translate("RXAnomaly", "Threshold: "))
        self.thresholdValueLabel.setText(_translate("RXAnomaly", ".999"))