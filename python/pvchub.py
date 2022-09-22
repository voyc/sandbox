''' pvchub.py '''
import os
import sys
from datetime import datetime
import importlib

def log(msg):
	sys.stdout.write(f'{datetime.now()} {msg}')

def pvchub(environ):
	log('wsgi starting')

	svcname = environ['PATH_INFO'][1:]
	module = importlib.import_module(svcname)
	response = module.pvc(environ)

	log('wsgi complete')
	return response
