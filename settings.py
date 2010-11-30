import os
import sys

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Administrator', 'admin@changeme.com'),
)

MANAGERS = ADMINS

# Path to the directory containing this settings.py file. For Windows, make
# sure to use Unix-style forward slashes, they are automatically translated.
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# Add this to assist with development. For example, I symlink my local
# clones of django-eve-db, djagno-eve-api, and django-eve-proxy into my
# apps dir so I can run them directly from there instead of installing them
# each time I make a change.
sys.path.insert(0, os.path.join(BASE_PATH, "apps"))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_eve',
        'USER': 'django_eve',
        'PASSWORD': 'django_eve',
        'HOST': '',
        'PORT': ''
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(BASE_PATH, 'media')
# When True, serve media through Django. This is only suitable for development,
# as Django is not meant to pipe static media out.
SERVE_MEDIA_LOCAL = True

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/amedia/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'CHANGETHIS'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.media',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_PATH, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'eve_proxy',
    'eve_db',
    'eve_api',
    'south',
)

# Optionally include django_extensions, if the user has it available.
try:
    import django_extensions
    INSTALLED_APPS += ('django_extensions',)
except ImportError:
    pass

# Path to the CCP SQLite DB dump.
EVE_CCP_DUMP_SQLITE_DB = os.path.join(BASE_PATH, 'ccp_dump.db')

# A user ID to use to get API information.
EVE_API_USER_ID = 1234567
# A user limited or full API key for API querying.
EVE_API_USER_KEY = 'CHANGE THIS TO YOUR API KEY'

"""
This makes any settings in local_settings.py take precedence over the ones
seen here. Make any local modifications to local_settings.py rather than
editing this file directly.
"""
try:
     from local_settings import *
except ImportError:
     pass
