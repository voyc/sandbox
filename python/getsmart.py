''' getsmart.py '''
import sys

def pvc(environ):
    message = 'It works, by golly!\n'
    version = 'Python %s\n' % sys.version.split()[0]
    response = '\n'.join([message, version])
    return response

