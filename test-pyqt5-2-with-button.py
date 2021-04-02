
# SORUCE :: https://levelup.gitconnected.com/pyqt5-tutorial-learn-gui-programming-with-python-and-pyqt5-df4225d2e3b8
# DOCS :: https://www.riverbankcomputing.com/static/Docs/PyQt5/

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton, QMessageBox
from PyQt5.QtCore import pyqtSlot

class App(QWidget):
	def __init__(self):
		super().__init__()
		self.title = 'Pyqt5 window'
		self.left = 10
		self.top = 10
		self.width = 300
		self.height = 300
		self.initUI()

	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		self.textbox = QLineEdit(self)
		self.textbox.move(80, 100)
		self.textbox.resize(150,40)
		self.label = QLabel(self)
		self.label.move(20, 20)
		self.label.setText("Hello Pyqt5")
		self.button = QPushButton('PyQt5 Button', self)
		self.button.move(100, 150)
		self.button.clicked.connect(self.on_click)
		self.show()

	@pyqtSlot()
	def on_click(self):
		self.reply = QMessageBox.question(self, 'Message', "Do you like Pyqt5", QMessageBox.Yes | QMessageBox.No,
										  QMessageBox.No)
		if self.reply == QMessageBox.Yes:
			print('Yes clicked.')
		else:
			print('No clicked.')


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())