from pathlib import Path
import os
import dj_database_url
from django.utils.translation import gettext_lazy as _


BASE_DIR = Path(__file__).resolve().parent.parent

# 🔐 Segurança
SECRET_KEY = 'django-insecure-_wkmbk%v*8)f!)-817ut606$!6$$$@03x(1m%htutxz422u7$'

DEBUG=True
# settings.py

ALLOWED_HOSTS = [
    'localhost',               # Para rodar localmente
    '127.0.0.1',                # Para rodar localmente
    'code-lai1.onrender.com',   # Seu domínio no Render
]

# 📦 Aplicações instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'modeltranslation',
    'paginas.apps.PaginasConfig',
]

# 🧱 Middlewares
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # para servir arquivos estáticos
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # para tradução
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'paginas.middleware.AcessoMiddleware',
]

ROOT_URLCONF = 'codehub.urls'

# 🎨 Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'codehub.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



# 🔐 Validação de senha
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 🌍 Internacionalização
LANGUAGE_CODE = 'pt'
TIME_ZONE = 'Africa/Luanda'
USE_I18N = True
USE_TZ = True

LANGUAGES = [
    ('pt', 'Português'),
    ('en', 'Inglês'),
    ('fr', 'Francês'),
    ('es', 'Espanhol'),
]

MODELTRANSLATION_DEFAULT_LANGUAGE='pt'

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

# 📁 Arquivos Estáticos e Mídia
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 📧 Configuração de Email (Gmail ou outro)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'nevesjosemar9@gmail.com'
EMAIL_HOST_PASSWORD = 'oyfh yvik hspl tbrz'

# 🧪 Configurações extras opcionais
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Cookies seguros
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_DOMAIN = "code-lai1.onrender.com"
CSRF_COOKIE_DOMAIN = "code-lai1.onrender.com"
SESSION_COOKIE_SAMESITE = "Lax"
CSRF_COOKIE_SAMESITE = "Lax"

# Redirecionar para HTTPS
SECURE_SSL_REDIRECT = True
