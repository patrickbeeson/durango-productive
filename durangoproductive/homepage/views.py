from django.views.generic import TemplateView
from django.core.exceptions import ObjectDoesNotExist

from portfolio.models import Project, Asset


class HomePageView(TemplateView):
    template_name = "homepage/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        try:
            context['featured_project'] = Project.featured.all()
        except ObjectDoesNotExist:
            context['featured_project'] = None
        return context
