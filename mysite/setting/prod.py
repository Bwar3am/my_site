from mysite.settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3x2ce32+4k3u6e_^0$5+mk(f_@nzq=!#xs3)nvotdype-$w*$_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['barsamaski.ir','www.barsamaski.ir']

#INSTALLED_APPS = []
SITE_ID = 1


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

STATIC_ROOT = BASE_DIR / "static"
MEDIA_ROOT = BASE_DIR  / "media"


STATICFILES_DIRS = [
    BASE_DIR / "statics",
]


#CSRF_COOKIE_SECURE = True
