from rest_framework import serializers

from django.utils.html import strip_tags, escape

from .models import Communication


class CommunicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Communication
        fields = (
            'pk',
            'name',
            'email',
            'message',
            'sent',
            'contacted',
            'contacted_date'
        )

    def create(self, validated_data):
        return Communication.objects.create(**validated_data)

    def validate_message(self, value):
        return escape(strip_tags(value))

    def validate(self, data):
        """
        Override the clean method to check for spam in honeypot.
        """
        honeypot = data.get('url', False)
        if honeypot:
            raise serializers.ValidationError(
                'Suspected spam in honeypot: {}'.format(honeypot),
                code='suspected spam',
                params={'value': honeypot}
            )
        return data
