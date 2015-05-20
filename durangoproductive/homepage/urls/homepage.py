from django.conf.urls import url

from homepage import views

"""
URL patterns for the homepage

"""

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
]
