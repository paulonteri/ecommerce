from backend.settings.base import *
from environs import Env

env = Env()

SECRET_KEY = env('SECRET_KEY')

DEBUG = env.bool('DEBUG')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env("DB_NAME"),
        'USER': env("DB_USER"),
        'PASSWORD': env("DB_PASSWORD"),
        'HOST': env("DB_HOST"),
        'PORT': env("DB_PORT"),
    }
}

# django-cors-headers
CORS_ORIGIN_WHITELIST = ['http://example.com', 'https://example.com']

# REST_FRAMEWORK
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES':
        ('knox.auth.TokenAuthentication',),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissions'
    ]
}

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Africa's talking
AFRICASTALKING_USERNAME = env('AFRICASTALKING_USERNAME')
AFRICASTALKING_API_KEY = env('AFRICASTALKING_API_KEY')
AFRICASTALKING_PAYMENT_PROD_NAME = env('AFRICASTALKING_PAYMENT_PROD_NAME')
AFRICASTALKING_CURRENCY = env('AFRICASTALKING_CURRENCY')
