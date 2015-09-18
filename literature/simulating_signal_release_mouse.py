from PyQt4 import QtGui, QtCore

class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)

        self.pushButtonSimulate = QtGui.QPushButton(self)
        self.pushButtonSimulate.setText("Simulate Mouse Release!")
        self.pushButtonSimulate.clicked.connect(self.on_pushButtonSimulate_clicked)

        self.layoutHorizontal = QtGui.QHBoxLayout(self)
        self.layoutHorizontal.addWidget(self.pushButtonSimulate)

    @QtCore.pyqtSlot()
    def on_pushButtonSimulate_clicked(self):
        mouseReleaseEvent = QtGui.QMouseEvent(
            QtCore.QEvent.MouseButtonRelease,
            self.cursor().pos(),
            QtCore.Qt.LeftButton,
            QtCore.Qt.LeftButton,
            QtCore.Qt.NoModifier,
        )

        QtCore.QCoreApplication.postEvent(self, mouseReleaseEvent)

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            print "Mouse Release"

        super(MyWindow, self).mouseReleaseEvent(event)

if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('MyWindow')

    main = MyWindow()
    main.show()

    sys.exit(app.exec_())