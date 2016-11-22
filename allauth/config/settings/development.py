    # coding: utf-8
from common import *

# DEBUG
# ------------------------------------------------------------------------------
DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0', '33.33.0.10']

# EMAIL using MailHog
# ------------------------------------------------------------------------------
EMAIL_PORT = 1025
EMAIL_HOST = 'localhost'
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# DATABASES Mysql
# ------------------------------------------------------------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'allauth_db',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost'
    }
}






# django-debug-toolbar
# ------------------------------------------------------------------------------
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
INSTALLED_APPS += ('debug_toolbar', )

INTERNAL_IPS = ['33.33.0.1', '127.0.0.1', '10.0.2.2', ]

DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}

# compressor
COMPRESS_ENABLED = False

# django-extensions
# ------------------------------------------------------------------------------
INSTALLED_APPS += ('django_extensions', )

# Custom project settings
# ------------------------------------------------------------------------------
