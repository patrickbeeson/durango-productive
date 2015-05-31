from django.forms import ModelForm, CharField, ValidationError
from django.utils.html import strip_tags, escape

from .models import Communication


class ContactForm(ModelForm):
    """
    Form allowing communication from users of the website.
    """
    url = CharField(required=False)

    def clean(self):
        """
        Override the clean method to check for spam in honeypot.
        """
        super(ContactForm, self).clean()
        honeypot = self.cleaned_data["url"]
        message = escape(strip_tags(self.cleaned_data["message"]))
        self.cleaned_data['message'] = message
        if honeypot:
            raise ValidationError(
                'Suspected spam in honeypot: {}'.format(honeypot),
                code='suspected spam',
                params={'value': honeypot}
            )
        return self.cleaned_data

    class Meta:
        model = Communication
        fields = ('name', 'email', 'message')
