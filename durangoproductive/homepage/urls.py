from django.conf.urls import url

from homepage.views import HomePageView

"""
URL patterns for the homepage

"""

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
]
