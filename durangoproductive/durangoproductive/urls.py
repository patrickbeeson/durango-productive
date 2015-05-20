from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

from .views import RobotsView

urlpatterns = [
    url(r'^$', include('homepage.urls.homepage')),
    url(r'^robots\.txt$', RobotsView.as_view()),
    url(r'^work/', include('portfolio.urls.projects')),
    url(r'^contact/', include('contact_form.urls.contact_form')),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls))
]

# Uncomment the next line to serve media files in dev.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [url(r'^__debug__/', include(debug_toolbar.urls))]
