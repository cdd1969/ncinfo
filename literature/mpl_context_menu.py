import sys
from PyQt4 import QtGui, QtCore
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from copy import deepcopy


class menuTest(QtGui.QWidget):
    def __init__(self, size=(5.0, 4.0), dpi=100):
        QtGui.QWidget.__init__(self)
        self.fig = Figure(size, dpi=dpi)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self)
        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addWidget(self.canvas)
        self.setLayout(self.vbox)

        self.ax = self.fig.add_subplot(111)
        self.ax.grid(True)

        self.canvas.mpl_connect('button_press_event', self.toggle_mpl_menu)
        self.mpl_menu_update(init=True)
 

        self.show()

    def toggle_mpl_menu(self, event):
        if event.button == 3 :  #if rmb is clicked
            canvasSize = event.canvas.geometry()
            Qpoint_click = event.canvas.mapToGlobal(QtCore.QPoint(event.x,canvasSize.height()-event.y))
            self.point = [event.xdata, event.ydata]
            self.canvasMenu.move(Qpoint_click)
            self.canvasMenu.show()

            print "picked point:", self.point

    def mpl_menu_picknext(self):
        print 'picking next cell...'
        self.point1 = deepcopy(self.point)
        # if "cancel" do not exist yet ...
        if self.mpl_menu_action_cancel not in self.canvasMenu.actions():
            print "adding cancel..."
            ca = QtGui.QAction('Cancel Selection', self)
            ca.triggered.connect(self.mpl_menu_cancelpick)
            self.canvasMenu.addAction(ca)
            self.mpl_menu_action_cancel = ca

            ca = QtGui.QAction('Generate crossection', self)
            ca.triggered.connect(self.mpl_menu_gencrosssection)
            self.canvasMenu.addAction(ca)
            self.mpl_menu_action_crosssection = ca


            self.mpl_menu_action_timeseries.setEnabled(False)
            self.mpl_menu_action_picknext.setEnabled(False)

    def mpl_menu_timeseries(self):
        print 'creating timeseries plot...'
        print "for point :", self.point

    def mpl_menu_cancelpick(self):
        print "canceling..."
        self.mpl_menu_update()

    def mpl_menu_gencrosssection(self):
        print "generate crossection..."
        print "point 1:", self.point1
        print "point 2:", self.point
        self.mpl_menu_update()

    def mpl_menu_update(self, init=False):
        if init:
            self.canvasMenu= QtGui.QMenu()

            ca = QtGui.QAction('Generate Timeseries plot', self)
            ca.triggered.connect(self.mpl_menu_timeseries)
            self.mpl_menu_action_timeseries = ca
            
            ca = QtGui.QAction('Pick 2nd cell...', self)
            ca.triggered.connect(self.mpl_menu_picknext)
            self.mpl_menu_action_picknext = ca
            
        self.canvasMenu.clear()
        
        self.canvasMenu.addAction(self.mpl_menu_action_timeseries)
        self.canvasMenu.addAction(self.mpl_menu_action_picknext)
        self.mpl_menu_action_cancel = None

        self.mpl_menu_action_timeseries.setEnabled(True)
        self.mpl_menu_action_picknext.setEnabled(True)




def main():    
    app = QtGui.QApplication(sys.argv)
    ex = menuTest()    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()