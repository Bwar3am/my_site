from mysite.settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3x2ce32+4k3u6e_^0$5+mk(f_@nzq=!#xs3)nvotdype-$w*$_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['barsamaski.ir','www.barsamaski.ir','127.0.0.1' ]

CSRF_TRUSTED_ORIGINS : ['https://barsamaski.ir']

#INSTALLED_APPS = []
SITE_ID = 1

AUTHENTICATION_BACKENDS = [
    'allauth.account.auth_backends.AuthenticationBackend',
    # ...
]



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

STATIC_ROOT = '/home/barsamas/public_html/static'
MEDIA_ROOT = '/home/barsamas/public_html/media'
STATICFILES_DIRS = [
    BASE_DIR / "statics",
]

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




LOGIN_REDIRECT_URL = '/'
# settings.py



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'barsamhassanzadehaski@gmail.com'  # Replace with your Gmail address
EMAIL_HOST_PASSWORD = 'aqkj mdxr mvzl leca'  
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
CSRF_COOKIE_SECURE = True





