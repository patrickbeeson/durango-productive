from braces.views import FormMessagesMixin

from django.views.generic import CreateView
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.core.mail import send_mail

from .forms import ContactForm

class ContactFormView(FormMessagesMixin, CreateView):
    """
    View to render the ContactForm and handle submissions.
    """
    form_class = ContactForm
    template_name = 'contact_form/contact_form.html'
    form_invalid_message = _(u'There was an error with your submission.')
    form_valid_message = _(u'Thank you for contacting Durango Productive. '
                           'We\'ll be in touch soon!')

    def get_success_url(self):
        "Redirect back to contact form view with message."
        return reverse('contact_form')

    def form_valid(self, form):
        "Send an email to site managers if the form is valid"
        form.clean_honeypot()
        message = "{name} / {email} said: ".format(
            name=form.cleaned_data.get('name'),
            email=form.cleaned_data.get('email'))
        message += "\n\n{0}".format(form.cleaned_data.get('message'))
        send_mail(
            subject='[Durango Productive] Contact form submission',
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=settings.LIST_OF_EMAIL_RECIPIENTS,
        )
        return super(ContactFormView, self).form_valid(form)
