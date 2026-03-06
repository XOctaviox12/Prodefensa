"""
Django settings for CIPOL project.
Configurado para PythonAnywhere + MySQL gratuito
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# ============================================================
# SEGURIDAD
# ============================================================
# ⚠️ Cambia esto por una clave segura y guárdala como variable
# de entorno en PythonAnywhere (no la dejes hardcodeada)
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-xnd)al^$$rv2*z22^$52h1rvbi#y6e*!@3oymgtolzy4*pcybh')

DEBUG = os.environ.get('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = [
    'XoctavioX.pythonanywhere.com',
    '127.0.0.1',
    'localhost',
]


# ============================================================
# APLICACIONES
# ============================================================
INSTALLED_APPS = [
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'inicio',
    'tienda',
    'cloudinary',
    'cloudinary_storage',
]

SITE_ID = 1


# ============================================================
# MIDDLEWARE
# ============================================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'CIPOL.urls'
WSGI_APPLICATION = 'CIPOL.wsgi.application'


# ============================================================
# TEMPLATES
# ============================================================
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


# ============================================================
# BASE DE DATOS
# - En LOCAL usa SQLite automáticamente (sin configurar nada)
# - En PythonAnywhere usa MySQL (cuando DB_HOST esté definido)
# ============================================================
# Variables de entorno a configurar en PythonAnywhere:
#   DB_NAME     → tuusuario$cipol  (el nombre que creaste en la pestaña Databases)
#   DB_USER     → tuusuario        (tu usuario de PythonAnywhere)
#   DB_PASSWORD → la contraseña que pusiste al crear la BD
#   DB_HOST     → tuusuario.mysql.pythonanywhere-services.com

if os.environ.get('DB_HOST'):
    # ✅ PRODUCCIÓN — PythonAnywhere con MySQL
    DATABASES = {
        'default': {
            'ENGINE':   'django.db.backends.mysql',
            'NAME':     'XoctavioX$CipolProdefensa',
            'USER':     'XoctavioX',
            'PASSWORD': 'Octavio_2801',  # ← Agrega DB_PASSWORD en las env vars de PythonAnywhere
            'HOST':     'XoctavioX.mysql.pythonanywhere-services.com',
            'PORT':     '3306',
            'OPTIONS': {
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
                'charset': 'utf8mb4',
            },
        }
    }
else:
    # 💻 LOCAL — SQLite (no necesita configuración extra)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# ============================================================
# ARCHIVOS ESTÁTICOS
# ============================================================
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# ============================================================
# MEDIA — Cloudinary (sin cambios, sigue igual)
# ============================================================
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME'),
    'API_KEY':    os.environ.get('CLOUDINARY_API_KEY'),
    'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET'),
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# ============================================================
# STRIPE
# ============================================================
DOMINIO = os.environ.get('DOMINIO', 'https://XoctavioX.pythonanywhere.com')
STRIPE_PUBLIC_KEY = os.environ.get('STRIPE_PUBLIC_KEY', 'pk_live_51S04LlCNPZDDg8Hg35G7MNfJzQ0htwkwbYfqSdca7HXJqkG6PGygqNjGYserxPYp8p30wKYgItgh2i9X7eyCCd9E00rigNWfcY')
STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY')
STRIPE_WEBHOOK_SECRET = os.environ.get('STRIPE_WEBHOOK_SECRET', 'whsec_agKDUHfSHJIo4ShKHp7mAr9wRDLcFD33')


# ============================================================
# EMAIL
# ============================================================
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# ============================================================
# AUTENTICACIÓN
# ============================================================
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# ============================================================
# INTERNACIONALIZACIÓN
# ============================================================
LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'America/Mexico_City'
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'