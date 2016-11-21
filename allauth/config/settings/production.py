# coding: utf-8
from common import *
import raven

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['allout.com']


# DATABASES = {
#     'default': {
#         'ENGINE': '',
#         'NAME': '',
#         'USER': '',
#         'PASSWORD': '',
#         'HOST': ''
#     }
# }


# Sentry settings

INSTALLED_APPS.append('raven.contrib.django.raven_compat')
RAVEN_CONFIG = {
    'dsn': 'Unknown',
    'release': raven.fetch_git_sha(
        os.path.dirname(os.path.join(BASE_DIR, '../'))
    ),
    'site': 'allout.com',
}

# Custom project settings
# ------------------------------------------------------------------------------
