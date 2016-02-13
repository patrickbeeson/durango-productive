from rest_framework.generics import ListAPIView, RetrieveAPIView

from django.views.generic import TemplateView

from .serializers import ProjectSerializer
from .models import Project


class ProjectListAPIView(ListAPIView):
    queryset = Project.public.all()
    serializer_class = ProjectSerializer
    lookup_field = 'slug'


class ProjectDetailFeaturedAPIView(RetrieveAPIView):
    queryset = Project.public.filter(is_featured=True)
    serializer_class = ProjectSerializer
    lookup_field = 'slug'


class ProjectDetailAPIView(RetrieveAPIView):
    queryset = Project.public.all()
    serializer_class = ProjectSerializer
    lookup_field = 'slug'


class ProjectDetailView(TemplateView):

    template_name = 'portfolio/project_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['slug'] = self.kwargs['slug']
        return context
