"""
Django settings for myshop project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information_shop on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
import dropbox

BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

ENVIRONMENT = os.environ.get('ENVIRONMENT', default='development')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.environ.get('DEBUG', default=0))

ALLOWED_HOSTS = ['hidden-castle-84780.herokuapp.com', 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'rest_framework',
    'shop',
    'cart',
    'orders',
    'accounts',
    'django_filters',
    'mathfilters',
    'django.contrib.postgres',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'myshop.urls'

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
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'myshop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '011288',
        'HOST': 'db',
        # 'HOST': 'localhost',
        'PORT': 5432

    }
}


REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS':(
        'django_filters.rest_framework.DjangoFilterBackend'
    )
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

DATE_FORMAT = 'd E Y'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/


STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_FINDERS = [
"django.contrib.staticfiles.finders.FileSystemFinder",
"django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DEFAULT_FILE_STORAGE = 'storages.backends.dropbox.DropBoxStorage'
dbx = dropbox.Dropbox('sl.BQuzVejRE3Y6Vz_NvqE809h3Mr1DZSY0W6DYCEwBzQqk6lLoKmBsDWypYLj8HjxCoAa2foXc9zMnpe5hkKugyyMoTpmGsvEYM3wyBfuSn7O0JdqH-cT3Ll0EqtV1tCcRUadyim0')
DROPBOX_OAUTH2_TOKEN = 'sl.BQt8OXVlcN-DEmhwJPvJL4LZFv-rbiSSLGJjdWSRUTRkHSe6J73km2k20bNB6G6DnkP-0PGVs61dHVzn7ozC3XXittwHs5W-rJMFseL6AnM_Bzj6bzpQmm5vwOZML0xcxJ1trwU'
DROPBOX_APP_KEY = 'nqgy6z1bm6rrpi4'
DROPBOX_APP_SECRET = '8a0877u1q8nanpf'
DROPBOX_OAUTH2_REFRESH_TOKEN = 'L-xGGujjpTQAAAAAAAAAAd_m7vFTxrhz69UmJk6EczOB44h9YF4DlEVzqXlgXOCj'
DROPBOX_ROOT_PATH = '/media/'
AUTHORIZATION_KEY = '5gPBsjzTqxkAAAAAAAAAJM-VC-uT4owK93SvLZY1ljg'

# curl -u nqgy6z1bm6rrpi4:8a0877u1q8nanpf \
# -d "code=5gPBsjzTqxkAAAAAAAAAJM-VC-uT4owK93SvLZY1ljg&grant_type=authorization_code" \
# -H "Content-Type: application/x-www-form-urlencoded" \
# -X POST "https://api.dropboxapi.com/oauth2/token"


# MEDIA_URL = '/product/'
# MEDIA_URL = 'https://product.dropbox.com/'
# MEDIA_ROOT = BASE_DIR / 'media/'
# MEDIA_ROOT = ''


CART_SESSION_ID = 'cart'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.yandex.by'
EMAIL_HOST_USER  =  os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587

# production
if ENVIRONMENT == 'production':
    SECURE_BROWSER_XSS_FILTER = True
    X_FRAME_OPTIONS = 'DENY'
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 3600
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Heroku
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)