from pydm import Display
from PyQt5 import QtGui, QtCore, QtWidgets
import epics
from epics import caget, caput

class Cavity(Display):
	#must be present in any pydm GUI
	def	ui_filename(self):
		return 'single_cavity.ui'

	#must be present in any pydm GUI
	def __init__(self, parent=None, args=None):
		super(Cavity, self).__init__(parent=parent, args=args)	
		

