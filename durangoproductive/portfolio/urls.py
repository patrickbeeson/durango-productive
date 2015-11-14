from django.conf.urls import url
from django.views.generic.base import TemplateView

from .views import ProjectListAPIView, ProjectDetailAPIView, ProjectDetailView
from .views import ProjectDetailFeaturedAPIView
"""
URL patterns for portfolio projects

"""

urlpatterns = [
    url(
        regex=r"^api/$",
        view=ProjectListAPIView.as_view(),
        name='portfolio_project_list_api'
    ),
    url(
        regex=r"^api/(?P<slug>[-\w]+)/$",
        view=ProjectDetailAPIView.as_view(),
        name='portfolio_project_detail_api'
    ),
    url(
        regex=r"^api/(?P<slug>[-\w]+)/$",
        view=ProjectDetailFeaturedAPIView.as_view(),
        name='portfolio_project_detail_featured_api'
    ),
    url(
        regex=r'^$',
        view=TemplateView.as_view(template_name='portfolio/project_list.html'),
        name='portfolio_project_list'
    ),
    url(
        regex=r'^(?P<slug>[-\w]+)/$',
        view=ProjectDetailView.as_view(),
        name='portfolio_project_detail'
    )
]
