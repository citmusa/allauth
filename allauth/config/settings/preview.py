# coding: utf-8
from common import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = ['preview.allout.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'allauth_db',
        'HOST': '0.0.0.0',
        'USER': 'allauth_usr',
        'PASSWORD': 'NotSet'
    }
}

# Custom project settings
# ------------------------------------------------------------------------------
