from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

from .views import RobotsView

urlpatterns = [
    url(r'^$', include('homepage.urls')),
    url(r'^robots\.txt$', RobotsView.as_view()),
    url(r'^work/', include('portfolio.urls')),
    url(r'^contact/', include('contact_form.urls')),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls))
]

# Enables auth for browsable API
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [url(r'^__debug__/', include(debug_toolbar.urls))]
