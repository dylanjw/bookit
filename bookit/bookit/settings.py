"""
Django settings for bookit project.

Generated by 'django-admin startproject' using Django 3.0.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import environ


root = environ.Path(__file__) - 2  # Set the base directory to two levels.
env = environ.Env(DEBUG=(bool, False), )  # set default values and casting
env.read_env(str(root.path('.env')))  # reading .env file

DEBUG = env.bool('DEBUG', default=True)
ENV = env('ENV', default='local')
DEBUG_ENVS = env.list('DEBUG_ENVS', default=['local', 'stage', 'test'])
IS_DEBUG_ENV = ENV in DEBUG_ENVS
HOSTNAME = env('HOSTNAME', default=socket.gethostname())
BASE_URL = env('BASE_URL', default='http://localhost:8000/')
SECRET_KEY = env('SECRET_KEY', default='YOUR-SupEr-SecRet-KeY')
ADMINS = (env.tuple('ADMINS', default=('TODO', 'todo@todo.net')))
BASE_DIR = root()

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['*'])
CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS', default=['localhost'])

EMAIL_BACKEND = ('django.core.mail.backends.console.EmailBackend' if ENV == 'local'
                 else 'django.core.mail.backends.smtp.EmailBackend')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'djreservations',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'djreservations.middleware.ReservationMiddleware',
]

DEFAULT_FROM_EMAIL = "mail@example.com"
EMAIL_HOST = "localhost"
EMAIL_PORT = "1025"

ROOT_URLCONF = 'bookit.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'bookit.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
LOGIN_REDIRECT_URL = 'home'
