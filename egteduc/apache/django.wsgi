import os,sys
sys.path.append('/home/gabriel/gteduc/egteduc')
os.environ['DJANGO_SETTINGS_MODULE'] = 'egteduc.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

