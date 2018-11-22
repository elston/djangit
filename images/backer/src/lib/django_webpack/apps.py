from io import open
import json
from django.apps import AppConfig

from .errors import BAD_MANIFEST_PATH


def webpack_cfg(*args, **kwargs):
    '''Test if config is compatible or not'''
    from django.conf import settings
    # ...
    if settings.MIGRATE_MODE:
        return []
    # ...
    check_failed = False

    manifest_path = getattr(settings, 'WEBPACK_MANIFEST_PATH', '')
    try:
        with open(manifest_path, encoding="utf-8") as f:
            settings.WEBPACK_MANIFEST = json.load(f)
    except TypeError:
        check_failed = True

    # ...
    errors = []
    if check_failed:
        errors.append(BAD_MANIFEST_PATH)
    # ..
    return errors


class DjangoWebpackConfig(AppConfig):
    name = 'django_webpack'
    verbose_name = "Django Webpack"

    def ready(self):
        from django.core.checks import register, Tags
        register(Tags.compatibility)(webpack_cfg)
