from django.views.generic import ListView, DetailView

from portfolio.models import Project


class BaseProjectMixin(object):
    model = Project


class ProjectList(BaseProjectMixin, ListView):
    pass


class ProjectDetail(BaseProjectMixin, DetailView):
    pass
