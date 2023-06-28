"""
WSGI config for Registration_Form project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application
project_home = '/home/Bonusree/Registration_Form'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# set environment variable to tell django where your settings.py is
# os.environ['DJANGO_SETTINGS_MODULE'] = 'Registration_Form.settings'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Registration_Form.settings')

application = get_wsgi_application()
