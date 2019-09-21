"""
Django settings for swagger_with_django project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!lq%g#06h(uu$3%al5!e571*)vkcv-tb=su3f#&+7!rax6(8v4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'rest_framework',
        'rest_framework_swagger',
        'cbv',
        'fbv'
]

MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'swagger_with_django.urls'

TEMPLATES = [
        {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [os.path.join(BASE_DIR, 'swagger_with_django/templates')]
                ,
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

WSGI_APPLICATION = 'swagger_with_django.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
        'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
REST_FRAMEWORK = {
        # Parser classes priority-wise for Swagger
        'DEFAULT_PARSER_CLASSES': [
                'rest_framework.parsers.FormParser',
                'rest_framework.parsers.MultiPartParser',
                'rest_framework.parsers.JSONParser',
        ],
}

SWAGGER_SETTINGS = {
        # For using django admin panel for authentication
        'USE_SESSION_AUTH': True,
        'LOGIN_URL': 'rest_framework:login',
        'LOGOUT_URL': 'rest_framework:logout',

        # For using other mechanisms for authentication ('basic' uses username/password)
        'SECURITY_DEFINITIONS': {
                'basic': {
                        'type': 'basic',
                },
        },

        # For validating your swagger schema(setting None to not validate)
        'VALIDATOR_URL': None,
}
