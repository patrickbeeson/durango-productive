from django.test import TestCase
from django.test import Client
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse

from .models import Communication
from .forms import ContactForm

class ContactFormTestCase(TestCase):
    """
    ContactForm unit tests
    """
    def setUp(self):
        self.client = Client()
        self.communication = Communication(
            name='Patrick Beeson',
            email='patrickbeeson@gmail.com',
            message='My test message'
        )

    def test_filling_honeypot_field_raises_error(self):
        contact_form = ContactForm(
            {
                'name': 'Patrick Beeson',
                'email': 'patrickbeeson@gmail.com',
                'message': 'My test message',
                'url': 'I can haz spambot?'
            },
            instance=self.communication
        )
        self.assertEqual(contact_form.is_valid(), False)
