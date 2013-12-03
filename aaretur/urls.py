from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import *
from django.contrib import admin

from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^jsi18n/(?P<packages>\S+?)/$', 'django.views.i18n.javascript_catalog'),
)

urlpatterns += patterns('',
    url(r'^$', TemplateView.as_view(template_name='app.html'))
)
if getattr(settings, 'DEVELOP', False):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

