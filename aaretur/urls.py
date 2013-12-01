from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include('smuggler.urls')), # put it before admin url patterns
    (r'^admin/', include(admin.site.urls)),
    (r'^jsi18n/(?P<packages>\S+?)/$', 'django.views.i18n.javascript_catalog'),
)

urlpatterns += patterns('',
    url(r'^handlevogn/', include('shoppingcart.urls')),
)
urlpatterns += patterns('',
    url(r'^sjekk_ut/', include('orders.urls')),
)
urlpatterns += patterns('',
    url(r'^tinymce/', include('tinymce.urls')),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += patterns('',
    url(r'^', include('cms.urls')),
)

