"""
Base Django settings for sandbox
"""
import os

BASE_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..",
)
DATA_DIR = os.path.join(BASE_DIR, "..", "data")


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cLiI!d*X=(%#?HyW]0!v"T-DFRk>JaukodHalf]&BLO5qkwB}S-_2'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sandbox.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'sandbox.wsgi.application'


# Database

DATABASES = {
    # Development default database engine use sqlite3
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DATA_DIR, 'db', 'db.sqlite3'),
    }
}
MIGRATION_MODULES = {}


# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'


"""
NOTE:
    * Every things above comes from default generated settings file (from Django startproject);
    * Every things below are needed settings for sandbox;
    * Don't edit default generated settings, instead override them below;
"""

# Absolute filesystem path to the directory that contain tests fixtures files
TESTS_FIXTURES_DIR = os.path.join('..', 'tests', 'data_fixtures')

INSTALLED_APPS = INSTALLED_APPS+(
    'crispy_forms',
    'crispy_forms_foundation',
    'sandbox.demo',
)


# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = os.path.join(DATA_DIR, "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
STATIC_ROOT = os.path.join(DATA_DIR, "static")

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

# Template dir
TEMPLATES[0]['DIRS'] = (os.path.join(BASE_DIR, "templates"),)
