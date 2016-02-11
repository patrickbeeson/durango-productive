from rest_framework.generics import CreateAPIView
from rest_framework import status
from rest_framework.response import Response

from django.core.urlresolvers import reverse
from django.conf import settings
from django.core.mail import send_mail

from .serializers import CommunicationSerializer
from django.contrib.sites.shortcuts import get_current_site


class CommunicationCreateAPIView(CreateAPIView):
    """
    View to create Communication objects via a POST method.
    """
    allowed_methods = [u'post']
    serializer_class = CommunicationSerializer

    def create(self, request, *args, **kwargs):
        "Override create method to send email."
        data = request.data
        serializer = self.get_serializer(data={
            'name': data.get('formData[name]'),
            'email': data.get('formData[email]'),
            'message': data.get('formData[message]')
        })
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        # Send email
        current_site = get_current_site(self.request)
        message = "{name} / {email} said: ".format(
            name=data.get('formData[name]'),
            email=data.get('formData[email]'))
        message += "\n\n{message}\n\n[View this message in the admin: http://{base_url}{admin_link}]".format(
            message=data.get('formData[message]'),
            base_url=current_site.domain,
            admin_link=reverse(
                'admin:contact_form_communication_change',
                args=(serializer.instance.id,))
        )
        send_mail(
            subject='[Durango Productive] Contact form submission',
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=settings.LIST_OF_EMAIL_RECIPIENTS,
        )
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers)
