"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 4.1.8.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import mimetypes
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url
import environ
env = environ.Env()
environ.Env.read_env()


PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [

    "menus",
    "blog",
    "home",
    "search",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail",
    "modelcluster",
    "taggit",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_htmx",
    'tailwind',
    'theme',
    'django_browser_reload',
    "wagtail.contrib.routable_page",
    'django_extensions',
    'wagtail_icon_picker',
    'storages',
    'sitesettings',
    'wagtail.contrib.settings',
    "django.contrib.sitemaps",
   
    
   
   
    'crispy_forms',
    'crispy_tailwind',
    
    
    
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    
    "django.middleware.common.CommonMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
    'home.middleware.VisitorMiddleware',
    
    "django_browser_reload.middleware.BrowserReloadMiddleware",
    "django_htmx.middleware.HtmxMiddleware",
    "home.middleware.SimpleMiddleware",
   
    
    
   
    
]

ROOT_URLCONF = "mysite.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(PROJECT_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                'wagtail.contrib.settings.context_processors.settings',
                'home.context_processors.visited_before',
            ],
        },
    },
]

WSGI_APPLICATION = "mysite.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

live_deploy = True
if live_deploy == True:

    ALLOWED_HOSTS = ['*', '']

    

    DATABASES = {
        'default': {
            'NAME': env("DATABASE_NAME"),
            'ENGINE': 'django.db.backends.postgresql',
            'USER': env('DATABASE_USER'),
            'PASSWORD': env('DATABASE_PASSWORD'),
            'HOST': env("DATABASE_HOST"),
            'PORT': env("DATABASE_PORT"),
        }
    }


elif live_deploy == False:

    ALLOWED_HOSTS = ['127.0.0.1']



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'testdb',
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASS'),
        'HOST': 'localhost',
        'PORT':  '5432',
    } 
}


# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, "static"),
]

# ManifestStaticFilesStorage is recommended in production, to prevent outdated
# JavaScript / CSS assets being served from cache (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/4.1/ref/contrib/staticfiles/#manifeststaticfilesstorage
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"



# Wagtail settings

WAGTAIL_SITE_NAME = "mysite"

# Search
# https://docs.wagtail.org/en/stable/topics/search/backends.html
WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.search.backends.database",
    }
}

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
WAGTAILADMIN_BASE_URL = "http://example.com"

TAILWIND_APP_NAME = 'theme'

INTERNAL_IPS = [
    "127.0.0.1", "172.17.0.1"
]

NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

X_FRAME_OPTIONS = 'SAMEORIGIN'

WAGTAILEMBEDS_RESPONSIVE_HTML = True

WAGTAILIMAGES_IMAGE_MODEL = 'home.CustomImage'



AWS_ACCESS_KEY_ID=env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY=env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME=env('AWS_STORAGE_BUCKET_NAME')
AWS_DEFAULT_ACL = None
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}



# s3 public media settings
PUBLIC_MEDIA_LOCATION = 'media'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"


AWS_S3_FILE_OVERWRITE = False


WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.search.backends.database',
    }
}


CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"
CRISPY_TEMPLATE_PACK = "tailwind"

mimetypes.add_type("application/javascript", ".js", True)

DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False,
}


ALLOWED_HOSTS = '192.168.1.254'

if 'DATABASE_URL' in os.environ:
    DATABASES['default'] = dj_database_url.config(
        conn_max_age=500,
        conn_health_checks=True,
    )

