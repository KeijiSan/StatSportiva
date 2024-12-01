"""
Django settings for StatSportiva project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path













# -------- MERCADO PAGO ----------


MERCADOPAGO_ACCESS_TOKEN = 'TEST-7300071637912413-112218-a3449faa2ddc8eb90e5a42914d5098f9-490058609'
MERCADOPAGO_PUBLIC_KEY = 'TEST-c6ef3eea-762e-41c4-9cfe-30172040878c'




# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent





# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-yw-!m38wd_z-06##@7)ej(*$ic2fb0&p7p@w*mc0)jb9g%bxx#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# settings.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'uenchiri@gmail.com'  # Cambia por tu correo
EMAIL_HOST_PASSWORD = 'mkxn wwvf dedj lvba'  # Contraseña de la app
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
DEFAULT_CONTACT_EMAIL = 'destinatario@correo.com'  # Correo que recibirá los mensajes


# Archivo JSON de las credenciales
GOOGLE_CREDENTIALS_FILE = 'basquetbol/client_secret_228538335100-nnv91uvl01i4iml1r6iv9old9pkiualm.apps.googleusercontent.com.json'

# Application definition

INSTALLED_APPS = [
    
    'widget_tweaks',
    'django.contrib.sites',  # Necesario para django-allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',  # Proveedor de Google
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'basquetbol',
]
SITE_ID = 1

CSRF_TRUSTED_ORIGINS = ['http://127.0.0.1', 'http://localhost']


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'StatSportiva.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates/basquetbol"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',  # Este debe estar incluido

            ],
        },
    },
]

WSGI_APPLICATION = 'StatSportiva.wsgi.application'
import os

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'basquetbol_torneo',  # Nombre de tu base de datos en XAMPP
        'USER': 'root',  # Usuario predeterminado de XAMPP
        'PASSWORD': '',  # Generalmente vacío por defecto, pero cambia si has establecido uno
        'HOST': 'localhost',  # XAMPP corre en localhost
        'PORT': '3306',  # Puerto predeterminado de MySQL
    }
}



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'es-es'  # Español de España, donde el formato común es DD/MM/YYYY
TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_REDIRECT_URL = '/proximo_partido/'
LOGIN_URL = 'login'
LOGOUT_REDIRECT_URL = '/proximo_partido/'


# Configuración de autenticación
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # Backend predeterminado
    'allauth.account.auth_backends.AuthenticationBackend',  # Backend de allauth
]
# Configuración de la autenticación de Google
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_SIGNUP_REDIRECT_URL = '/proximo_partido/'
SOCIALACCOUNT_LOGIN_ON_GET = True

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {'access_type': 'online'},
    }
}
