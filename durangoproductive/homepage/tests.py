import datetime
import factory
import random
import string
from rest_framework.test import APIRequestFactory
from test_plus.test import TestCase

from portfolio.models import Project


def random_string(length=10):
    return u''.join(random.choice(string.ascii_letters) for x in range(length))


class ProjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Project

    client_name = factory.LazyAttribute(lambda t: random_string())
    slug = 'some-test'
    description = factory.LazyAttribute(lambda t: random_string())
    is_public = True
    completion_date = datetime.datetime.now()


class HomePageViewTests(TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.featured_project = ProjectFactory.create(
            is_featured=True,
        )
        self.not_featured_project = ProjectFactory.create()

    def test_featured_project_is_in_context(self):
        self.get_check_200('home')
        self.assertInContext('slug')
        self.get('home')
        slug = self.get_context('slug')
        self.assertEqual(slug, self.featured_project.slug)

    def test_not_featured_project_is_not_in_context(self):
        self.get('home')
        slug = self.get_context('slug')
        self.assertNotEqual(slug, self.not_featured_project)

    def tearDown(self):
        self.featured_project.delete()
        self.not_featured_project.delete()
