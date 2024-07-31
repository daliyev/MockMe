from pathlib import Path
from dotenv import load_dotenv
import os
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-55!nkj^2mc*$6p7q4xkit^ueqwkeen0wc$s6dp+$t(uhtvr3++'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

EMAIL_HOST_NAME = os.getenv('EMAIL_HOST_NAME')
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"


INSTALLED_APPS = [
    # local
    'dtmtest',
    'results',
    'accounts',
    'advertisement',
    'dtmtests',
    # third
    'psycopg2',
    'jazzmin',
    'corsheaders',
    'drf_yasg',
    'rest_framework',
    'django_extensions',
    'whitenoise',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

CORS_ALLOWED_ORIGINS = [
    "http://*",
    "https://*",
]


CORS_ALLOW_ALL_ORIGINS: True
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'authorizations',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]



ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('NAME'),
        'USER': 'talabauzuser',
        'PASSWORD': os.getenv('PASSWORD'),
        'HOST': '127.0.0.1',
        'PORT': '5432',
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

AUTHENTICATION_BACKENDS = [
    'accounts.authentication.EmailAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

JAZZMIN_SETTINGS = {
    "site_title": "MockMe",
    "site_header": "MockMe",
    "site_brand": "MockMe",
    "order_with_respect_to": [
        "auth",
        "about",
        "about.workersmodel",
        "about.tradeunion",
        "about.about",
        "about.Statistics",
        "executive",
        "council",
        "post",
        "gallery",
        "doc",
        "doc.doccategory",
        "normative_doc",
        "vacancy",
        "affiliates",
        "teritory_division",
        "virtual_reception",
        "feedback",
        "information",
        "useful_link",
        "faq",
    ],
    "icons": {
        "auth.Group": "fas fa-user-friends",
        "auth.User": "fas fa-users",
        "about.WorkersModel": "fas fa-user-tie",
        "about.TradeUnion": "fas fa-user-tie",
        "about.About": "fas fa-info-circle",
        "about.Statistics": "fas fa-chart-pie",
        "affiliates.affiliates": "fas fa-people-arrows",
        "council.council": "fas fa-user-shield",
        "council.categorycouncil": "fas fa-align-justify",
        "doc.doc": "fas fa-file-alt",
        "doc.doccategory": "fas fa-align-justify",
        "executive.ExecutiveApparatus": "fas fa-user-tie",
        "faq.faq": "fas fa-question",
        "feedback.feedback": "fas fa-phone",
        "gallery.photogallery": "fas fa-images",
        "gallery.videogallery": "fas fa-video",
        "information.InfoCategory": "fas fa-align-justify",
        "information.executiveapparatusinformation": "fas fa-phone-volume",
        "normative_doc.NormativeDocCategory": "fas fa-align-justify",
        "normative_doc.NormativeDocument": "fas fa-print",
        "post.category": "fas fa-align-justify",
        "post.postmodel": "fas fa-newspaper",
        "teritory_division.TerritoryDivision": "fas fa-map-marked-alt",
        "useful_link.usefullink": "fas fa-handshake",
        "vacancy.vacancy": "fas fa-user-plus",
        "virtual_reception.VirtualReception": "fas fa-envelope",
    }
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

GRAPH_MODELS ={
    'all_applications': True,
    'graph_models': True,
}