from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView

# ..
urlpatterns = [
    # ..Pages
    url(r'^$',
        TemplateView.as_view(template_name='main.html'),
        name='main'),

    # ...Admin
    url(r'^admin/', admin.site.urls),
    
]

