from PyQt5 import QtWidgets
import os
from PyQt5.uic import loadUi
from ...engine.common.logging_utils import logger

class FrameStocks(QtWidgets.QWidget):
    def __init__(self,logic,parent=None):
        super(FrameStocks,self).__init__(parent)

        current_path = os.path.abspath(__file__)
        father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
        father_path = os.path.abspath(os.path.dirname(father_path) + os.path.sep + ".")
        file = father_path + '/ui/stocks.ui'
        loadUi(file,self)

        self.mgr = logic
        logic.frame_symbols = self
        logic.signal.connect(self.on_events)

    def get_data(self):
        text = self.edit_symbols.toPlainText()
        symbols = text.split('\n')
        logger.info(symbols)

    def on_events(self,data):
        pass
