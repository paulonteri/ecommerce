from backend.settings.base import *

SECRET_KEY = '6h03)d($%+c4r#p65#ctnk3*u21^v@q+*e^ue0+llrq%zv(94z'

DEBUG = True

ALLOWED_HOSTS = ["*", ]

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# django-cors-headers

CORS_ORIGIN_ALLOW_ALL = True

# REST_FRAMEWORK
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES':
        ('knox.auth.TokenAuthentication',),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ]
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

# Africa's talking
AFRICASTALKING_USERNAME = os.environ.setdefault('AFRICASTALKING_USERNAME', 'sandbox')
AFRICASTALKING_API_KEY = os.environ.setdefault('AFRICASTALKING_API_KEY', 'AFRICASTALKING_API_KEY')
AFRICASTALKING_PAYMENT_PROD_NAME = os.environ.setdefault('AFRICASTALKING_PAYMENT_PROD_NAME', 'AFRICASTALKING_PAYMENT_PROD_NAME')
AFRICASTALKING_CURRENCY = os.environ.setdefault('AFRICASTALKING_USERNAME', 'KES')
