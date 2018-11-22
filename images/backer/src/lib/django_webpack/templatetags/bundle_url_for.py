from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def bundle_url_for(name):
    return mark_safe('%s/%s'%(
        settings.WEBPACK_BUNDLE_URL, 
        settings.WEBPACK_MANIFEST[name]))
