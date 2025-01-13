from dotenv import load_dotenv
from pathlib import Path
import os

from django.core.management.utils import get_random_secret_key

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY", get_random_secret_key())

DEBUG = os.getenv("DEBUG", "False") == "True"

if DEBUG:
    ALLOWED_HOSTS = os.getenv(
        "DEBUG_TRUE_ALLOWED_HOSTS",
        "localhost"
    ).split(",")
else:
    ALLOWED_HOSTS = os.getenv(
        "DEBUG_FALSE_ALLOWED_HOSTS",
        "localhost"
    ).split(",")

if DEBUG:
    CSRF_TRUSTED_ORIGINS = os.getenv(
        "DEBUG_TRUE_CSRF_TRUSTED_ORIGINS",
        "http://localhost,http://127.0.0.1"
    ).split(",")
else:
    CSRF_TRUSTED_ORIGINS = os.getenv(
        "DEBUG_FALSE_CSRF_TRUSTED_ORIGINS",
        "http://localhost,http://127.0.0.1"
    ).split(",")

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'drf_yasg',
    'rest_framework',
    'corsheaders',
    'django_filters',
    'employees.apps.EmployeesConfig',
    'ratings.apps.RatingsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if DEBUG:
    MIDDLEWARE += [
        "querycount.middleware.QueryCountMiddleware",
    ]

    QUERYCOUNT = {
        "IGNORE_REQUEST_PATTERNS": [r"^/admin/"],
        "IGNORE_SQL_PATTERNS": [r"silk_"],
        "DISPLAY_DUPLICATES": 2,
    }

ROOT_URLCONF = 'dashboard_backend.urls'

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

WSGI_APPLICATION = 'dashboard_backend.wsgi.application'

if DEBUG:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": os.getenv("DB_ENGINE", default="django.db.backends.postgresql"),
            "NAME": os.getenv("POSTGRES_DB", default="dashboard"),
            "USER": os.getenv("POSTGRES_USER", default="postgres"),
            "PASSWORD": os.getenv("POSTGRES_PASSWORD", default="mysecretpassword"),
            "HOST": os.getenv("DB_HOST", default="db"),
            "PORT": os.getenv("DB_PORT", default=5432),
        }
    }


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


LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ORIGIN_ALLOW_ALL = True

CORS_URLS_REGEX = r'^/api/.*$'

# CORS_ALLOWED_ORIGINS = [
#     'http://localhost:3000',
# ]


REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": None,
}
