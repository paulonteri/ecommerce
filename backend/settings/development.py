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

# Africa's talking
AFRICASTALKING_USERNAME = os.environ.setdefault('AFRICASTALKING_USERNAME', 'sandbox')
AFRICASTALKING_API_KEY = os.environ.setdefault('AFRICASTALKING_API_KEY', 'AFRICASTALKING_API_KEY')
AFRICASTALKING_PAYMENT_PROD_NAME = os.environ.setdefault('AFRICASTALKING_PAYMENT_PROD_NAME',
                                                         'AFRICASTALKING_PAYMENT_PROD_NAME')
AFRICASTALKING_CURRENCY = os.environ.setdefault('AFRICASTALKING_USERNAME', 'KES')

INTERNAL_IPS = ('127.0.0.1',)

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INSTALLED_APPS += [
    'debug_toolbar',
]

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

MEDIA_ROOT = os.path.join(BASE_DIR, "./media")
