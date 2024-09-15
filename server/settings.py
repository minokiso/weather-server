import datetime
from datetime import timedelta
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-&06_1raur2x8fo%g@!nb49hkb$%m2^2wam-)&lu5c1l6m7gbc$'

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'apps.public',
]
CORS_ALLOW_ALL_ORIGINS = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
]

AUTHENTICATION_BACKENDS = []

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
    ],
    'DEFAULT_PERMISSION_CLASSES': [
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter'
    ]
}

ROOT_URLCONF = 'server.urls'

WSGI_APPLICATION = 'server.wsgi.application'

try:
    from conf import _DATABASES

    DATABASES = _DATABASES
except Exception as e:
    print("未找到自定义配置文件，使用默认sqlite数据库")
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

# USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

TRANSACTION_AVAILABLE_DURATION = datetime.timedelta(minutes=30)
