from django.forms import ModelForm, CharField, ValidationError, TextInput

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
        value = self.cleaned_data["url"]
        if value:
            raise ValidationError(
                'Suspected spam in honeypot: {}'.format(value),
                code='suspected spam',
                params={'value': value}
            )
        return self.cleaned_data

    class Meta:
        model = Communication
        fields = ('name', 'email', 'message')
