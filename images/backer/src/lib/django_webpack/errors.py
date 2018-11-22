from django.core.checks import Error
from django.conf import settings


BAD_CONFIG_ERROR = Error(
    'Error while parsing DJANGO_WEBPACK configuration',
    hint='Is DJANGO_WEBPACK config valid?',
    obj='django.conf.settings.DJANGO_WEBPACK',
    id='django-webpack-loader.E001',
)


BAD_MANIFEST_PATH = IOError(
    'Error reading {0}. Are you sure webpack has generated '
    'the file and the path is correct?'.format(
        settings.WEBPACK_MANIFEST_PATH)
)