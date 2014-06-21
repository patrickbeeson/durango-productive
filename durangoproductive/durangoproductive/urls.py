from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()

from .views import HomePageView, RobotsView

urlpatterns = patterns(
    '',
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^robots\.txt$', RobotsView.as_view()),
    url(r'^work/', include('portfolio.urls.projects')),
    url(r'^contact/', include('contact_form.urls')),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls))
)

# Uncomment the next line to serve media files in dev.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            )
