"""
WSGI config for travel_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import sys

path = '/home/123yuvashree/Travel_booking_website'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'Travel_booking_website.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
