from django.conf.urls import url

from views import ContactFormView

"""
URL patterns for the contact form

"""

urlpatterns = [
    url(r'^$', ContactFormView.as_view(), name='contact_form'),
]
