import logging
from ast import literal_eval

from algorithms.Algorithm import AlgorithmController
from algorithms.RXAnomaly.views.RXAnomaly_ui import Ui_RXAnomaly

from PyQt5.QtGui import QFontDatabase, QFont, QIcon, QColor
from PyQt5.QtCore import QFile, QTextStream, QTranslator, QLocale, QThread, pyqtSlot
from PyQt5.QtWidgets import QWidget,QApplication, QColorDialog, QMessageBox

class RXAnomaly(QWidget, Ui_RXAnomaly, AlgorithmController):
    """Main Window."""

    def __init__(self):
        QWidget.__init__(self)
        AlgorithmController.__init__(self, 'RXAnomaly', 10)
        self.setupUi(self)
        self.thresholdSlider.valueChanged.connect(self.updateThreshold)

    def getOptions(self):
        options = dict()
        options['threshold'] = float(self.thresholdValueLabel.text())
        return options

    def updateThreshold(self):
        if self.thresholdSlider.value() == 0:
            self.thresholdValueLabel.setText('0')
        elif self.thresholdSlider.value() == 1000:
            self.thresholdValueLabel.setText('1')   
        else:
            self.thresholdValueLabel.setText("."+str(self.thresholdSlider.value()))
    
    def validate(self):
        return None;

    def loadOptions(self, options):
        if 'threshold' in options:
            self.thresholdValueLabel.setText(str(options['threshold']))
            self.thresholdSlider.setProperty("value", int(float(options['threshold'])*1000))