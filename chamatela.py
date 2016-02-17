from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from main import *

app = QtWidgets.QApplication(sys.argv)
dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(dialog)
dialog.show()
sys.exit(app.exec_())