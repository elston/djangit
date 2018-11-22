import json
import os
import sys
import datetime
# ..
from django.core.exceptions import ImproperlyConfigured

# ...
def get_env_variable(var_name, allow_none=False):
    try:
        return os.environ[var_name]
    except KeyError:
        if allow_none is False:
            err_msg = "Set the %s environment variable" % var_name
            raise ImproperlyConfigured(err_msg)
        return None


DEBUG = False
MIGRATE_MODE = get_env_variable('MIGRATE_MODE',allow_none=True)
if MIGRATE_MODE:
    MIGRATE_MODE = json.loads(MIGRATE_MODE)


# ...dir
# =====================================
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)))

PROJECT_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__))))

# ...key
# =====================================
SECRET_KEY = '5rt2+=ffhi0ge9^x&ll*!_fz+84%!$l5m-d=13k(+^kys%l@ye'


# ...hosts
# =====================================
ALLOWED_HOSTS = [
    'localhost',
]

# ...databases
# =====================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_env_variable('DB_NAME'),
        'USER': get_env_variable('DB_USER'),
        'PASSWORD': get_env_variable('DB_PASSWORD'),
        'HOST': get_env_variable('DB_HOST'),
        'PORT': get_env_variable('DB_PORT'),
    },
}

# ...apps
# =====================================
INSTALLED_APPS = [

    # default
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # app
    # ...

    # other
    'django_webpack',
]

# ...middleware
# =====================================
MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ...templates
# =====================================
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [
        os.path.join(BASE_DIR, 'templates'),
    ],
    # 'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ],
        'loaders': [
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        ],
    },
}]


# ...auth
# =====================================
AUTH_PASSWORD_VALIDATORS = [{
    'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
},{
    'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
},{
    'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
},{
    'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
}]


# ...logs
# =====================================
LOG_FILE = os.path.join(BASE_DIR, '.logs/django.log')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format' : '[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s',
            'datefmt' : '%d/%b/%Y %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    }, 
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': LOG_FILE,
        },
    },
    'loggers': {
        'crowdface': {
            'handlers': ['console','file'],
            'level': 'DEBUG',
            'propagate': True,
            'formatter': 'standard',
        },
    },
}


# ...misc
# =====================================
LANGUAGE_CODE = 'ru-RU'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# ...app conf
# =====================================
ROOT_URLCONF = 'urls'
WSGI_APPLICATION = 'wsgi.application'
STATIC_URL = '/static/'


# ...external lib paths
# =====================================
sys.path.insert(0, 
    os.path.join(BASE_DIR, 'lib')
)


# ...webpack
# =====================================

WEBPACK_MANIFEST_PATH = os.path.join(
    PROJECT_DIR, 'fronter', 'build','manifest.json'
)
WEBPACK_BUNDLE_URL = '/build'
WEBPACK_MANIFEST = None


