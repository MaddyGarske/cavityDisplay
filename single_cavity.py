from PyQt5 import QtGui
#import meme.archive
#import epics
#from datetime import datetime
#import time
#from pytz import utc, timezone
#from random import randint
#from sys import argv, exit
from pydm import Display
#from PyQt5.QtCore import QDateTime, Qt #QTimer, QObject, pyqtSignal, QDate
#from urllib2 import urlopen
from json import load

class Cavity(Display):

#below four lines must be present in any pydm GUI
	def __init__(self, parent=None, args=None):
		super(Cavity, self)._init_(parent=parent, args=args)	
		
	def	ui_filename(self):
		return 'single_cavity.ui'
