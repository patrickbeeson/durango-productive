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


class PortfolioAPITests(TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.project = ProjectFactory.create()

    def test_project_list_api(self):
        "Ensure calling project list api returns expected data."
        response = self.get('portfolio_project_list_api',
                            extra={'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'})
        # We should get one project back
        self.assertEqual(response.json()[0]['pk'], self.project.pk)

    def test_project_detail_api(self):
        "Ensure calling project detail api returns expected data."
        response = self.get('portfolio_project_detail_api',
                            slug=self.project.slug,
                            extra={'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'})
        # We should get one project back
        self.assertEqual(response.json()['pk'], self.project.pk)

    def test_get_project_detail_api_method(self):
        "Ensure we can get the project absolute url via the api."
        response = self.get('portfolio_project_detail_api',
                            slug=self.project.slug,
                            extra={'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'})
        # We should return the absolute url for the project
        self.assertEqual(response.json()['project_detail']['self'],
                         'http://testserver/work/some-test/')

    def test_project_detail_featured_api(self):
        "Ensure calling project detail featured api returns expected data."
        self.project.is_featured = True
        response = self.get('portfolio_project_detail_featured_api',
                            slug=self.project.slug,
                            extra={'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'})
        # We should get one project back
        self.assertEqual(response.json()['pk'], self.project.pk)

    def tearDown(self):
        [p.delete() for p in Project.objects.all()]


class ProjectManagerTests(TestCase):

    def setUp(self):
        self.project = ProjectFactory.create()
        self.not_public_project = ProjectFactory.create(is_public=False)

    def test_public_project_manager_returns_correctly(self):
        self.assertTrue(self.not_public_project not in Project.public.all())

    def tearDown(self):
        [p.delete() for p in Project.objects.all()]
