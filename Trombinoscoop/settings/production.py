import os

import dj_database_url

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration


from . import *

DEBUG = False

SECRET_KEY = os.environ.get('SECRET_KEY', '+xz#p9=p*ahiz4l0pnp(lyhb^6gxe^7i^$=#$uj&(bs(v6cg=_')

ALLOWED_HOSTS = [
    'trombinoscoop-2.herokuapp.com',  
]

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware',]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DATABASES['default'].update(dj_database_url.config())

sentry_sdk.init(
    dsn="https://1199978d2b974d85b7523150181a2a7c@sentry.io/1291046",
    integrations=[DjangoIntegration()]
)

INSTALLED_APPS += ['django_extensions',]
