from django.views.generic import TemplateView
from django.core.exceptions import ObjectDoesNotExist

from portfolio.models import Project


class HomePageView(TemplateView):
    template_name = "homepage/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['slug'] = Project.public.filter(
                is_featured=True).latest('completion_date').slug
        except ObjectDoesNotExist:
            context['slug'] = None
        return context
