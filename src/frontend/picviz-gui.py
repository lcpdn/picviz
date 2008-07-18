#!/usr/bin/env python
#
######################
# Frontend for Picviz
######################
# (C) 2008 Sebastien Tricaud
#

# Python libs
import os
import sys
import time

# QT
from PyQt4 import QtCore, QtGui

# Picviz
import picviz

# UI
from ui_picviz import Ui_MainWindow


pcvfile = "../../samples/test2.pcv"
axiswidth = 200

ui = Ui_MainWindow()
scene = QtGui.QGraphicsScene()


class PicvizApp(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

def addLines(filename):

	pen = QtGui.QPen()
	pen.setColor(QtCore.Qt.black)

	data = picviz.ParseLines(filename)

	# Ugly crap to cheat python bindings, should write a AxisNumberGet() function latter
	axisnb = 0
	for line in data:
		axisnb = 0
		for plot in line:
			axisnb = axisnb + 1

	i = 1
	while i <= axisnb:
		scene.addLine(i * axiswidth, 0, i * axiswidth, 500, pen)
		i = i + 1

	for line in data:
		plotnb = 0
		for plot in line:
			plotnb = plotnb + 1
			if plotnb != axisnb:
				scene.addLine(plotnb * axiswidth, 500 - line[plotnb-1], (plotnb + 1) * axiswidth, 500 - line[plotnb])

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	window = QtGui.QMainWindow()

	ui.setupUi(window)

	scene = QtGui.QGraphicsScene(ui.graphicsView)
	ui.graphicsView.setScene(scene)
	scene.setSceneRect(0, 0, 875, 500)


	window.show()

	addLines(pcvfile)

	sys.exit(app.exec_())

