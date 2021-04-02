
# SOURCE: https://levelup.gitconnected.com/pyqt5-tutorial-learn-gui-programming-with-python-and-pyqt5-df4225d2e3b8

#importing libraries
import sys
from PyQt5.QtWidgets import QApplication, QWidget
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(300,300)
    w.setWindowTitle('Zoltan Dul Pyqt5')
    w.show()
    sys.exit(app.exec_())

# QWidget is the base class of the UI in pyqt5, everything you see in a desktop application like Buttons,
#   search bar, drop-down menu and etc are widgets so you can say that widgets are built in a widget.
#   This will help you to build complex user interfaces by nesting the widgets.
# w.resize(300,300) is a Qwidget class method that resizes your window to any height and width.
#   They take two parameters, the first is the x which denotes width and the second is y which denotes height.
# w.setwindowtitle(“Basic pyqt5”) is a Qt widget class method that takes a string argument as
#   a parameter and changes your desktop application title bar.
# w.show() is the Qtwidget method that shows the window on your screen.
# sys.exit(app.exec_()) will start the Qt/C++ event loop as we know the Qt is purely built-in C++ language
#   and app.exec_() will simply start the loop mechanism of the app and you cannot close
#   the desktop application by simply pressing ctrl + c as you do in other applications you need to click
#   on the close button of the application.