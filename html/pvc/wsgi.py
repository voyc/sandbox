''' wsgi.py '''
import sys
import os
sys.path.append( os.environ['LOCAL_MODULE_DIR'])
import pvchub
def application(environ, start_response):
	start_response('200 OK', [('Content-Type', 'text/plain')])
	sys.stdout.write('open log')
	response = pvchub.pvchub(environ)
	return [response.encode()]
