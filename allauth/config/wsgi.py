"""
WSGI config for Allauth Test project.
It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os

from django.core.wsgi import get_wsgi_application

environment = os.environ.get('PROJECT_ENV', 'development')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.%s" % environment)

application = get_wsgi_application()
