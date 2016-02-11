from test_plus.test import TestCase


class ContactFormAPITests(TestCase):
    """
    ContactForm API unit tests.
    """
    def test_contact_form_view(self):
        response = self.get('contact_form')
        self.response_200(response)

    def test_communication_create_endpoint(self):
        "Ensure we can issue a successful POST to API endpoint."
        data = {
            'name': 'Patrick Beeson',
            'email': 'patrickbeeson@gmail.com',
            'message': 'Some message, eh?'
        }
        response = self.post('communication_create',
                             data=data,
                             extra={'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'})
        self.response_200(response)
