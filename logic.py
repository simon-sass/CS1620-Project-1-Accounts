from accounts import *
from gui import *
from PyQt6.QtWidgets import *

class Logic(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)