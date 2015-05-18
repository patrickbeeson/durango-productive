from django.forms import ModelForm, CharField, ValidationError, HiddenInput

from .models import Communication


class ContactForm(ModelForm):
    """
    Form allowing communication from users of the website.
    """
    honeypot = CharField(
        required=False,
        label='If you enter anything in this field your comment will be '
              'treated as spam',
        widget=HiddenInput(attrs={'style': 'display: none;'})
    )

    def clean_honeypot(self):
        """Check that nothing's been entered into the honeypot."""
        value = self.cleaned_data["honeypot"]
        if value:
            raise ValidationError(self.fields["honeypot"].label)
        return value

    class Meta:
        model = Communication
        fields = ('name', 'email', 'message')
