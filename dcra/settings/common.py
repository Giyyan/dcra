import os
from os.path import basename
import djcelery

djcelery.setup_loader()

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SITE_NAME = basename(BASE_DIR)

########## SITE CONFIGURATION
# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []
########## END SITE CONFIGURATION

########## DEBUG CONFIGURATION
DEBUG = False

TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


########## MANAGER CONFIGURATION
ADMINS = (
    ('Giyyan', 'karbanovich.andrey@gmail.com'),
)

MANAGERS = ADMINS
########## END MANAGER CONFIGURATION


########## SECRET CONFIGURATION
SECRET_KEY = 'x*6ag5r8_ekmd85%xwj4ftrinex3ocuo+$o1l0&p132@r2j=xb'
########## END SECRET CONFIGURATION


########## END APP CONFIGURATION
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'south',
    'djcelery',
)

LOCAL_APPS = (
    'dcra.apps.posts',
    # 'dcra.apps.tasks',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
########## END APP CONFIGURATION


########## MIDDLEWARE CONFIGURATION
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
########## END MIDDLEWARE CONFIGURATION


########## URL CONFIGURATION
ROOT_URLCONF = '%s.urls' % SITE_NAME
########## END URL CONFIGURATION

WSGI_APPLICATION = '%s.wsgi.application' % SITE_NAME


########## DATABASE CONFIGURATION
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
    }
}
########## END DATABASE CONFIGURATION


########## GENERAL CONFIGURATION
LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True
########## END GENERAL CONFIGURATION


########## MEDIA CONFIGURATION
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = '/media/'
########## END MEDIA CONFIGURATION


########## STATIC FILE CONFIGURATION
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
########## END STATIC FILE CONFIGURATION


########## TEMPLATE CONFIGURATION
TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'),)

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)
########## END TEMPLATE CONFIGURATION


########## CELERY CONFIGURATION
BROKER_URL = 'amqp://guest@127.0.0.1:5672//'

CELERY_RESULT_BACKEND = "amqp"
CELERY_TASK_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']  # Ignore other content
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Europe/Kiev'
CELERY_ENABLE_UTC = True

CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"
########## END CELERY CONFIGURATION


########## TASTYPIE CONFIGURATION
TASTYPIE_DEFAULT_FORMATS = ['json']
########## END TASTYPIE CONFIGURATION


########## LOGGING CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
########## END LOGGING CONFIGURATION