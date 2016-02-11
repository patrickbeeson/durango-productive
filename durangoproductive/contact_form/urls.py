from django.conf.urls import url
from django.views.generic.base import TemplateView

from .views import CommunicationCreateAPIView

"""
URL patterns for the contact form

"""

urlpatterns = [
    url(
        regex=r'^$',
        view=TemplateView.as_view(
            template_name='contact_form/contact_form.html'),
        name='contact_form'
    ),
    url(
        regex=r'^api/create/$',
        view=CommunicationCreateAPIView.as_view(),
        name='communication_create'
    ),
]
