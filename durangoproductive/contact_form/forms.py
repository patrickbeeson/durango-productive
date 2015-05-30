from django.forms import ModelForm, CharField, ValidationError, TextInput

from .models import Communication


class ContactForm(ModelForm):
    """
    Form allowing communication from users of the website.
    """
    url = CharField(required=False)

    def clean_honeypot(self):
        """Check that nothing's been entered into the fake-url field/honeypot.
        """
        value = self.cleaned_data["url"]
        if value:
            raise ValidationError(self.fields["url"].label)
        return value

    class Meta:
        model = Communication
        fields = ('name', 'email', 'message')
