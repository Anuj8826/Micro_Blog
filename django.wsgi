import os
import sys
 
path='/django_test'
 
if path not in sys.path:
sys.path.append(path)
 
os.environ['DJANGO_SETTINGS_MODULE'] = 'django_test.settings'
 
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
