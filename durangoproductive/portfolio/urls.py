from django.conf.urls import url

from portfolio.views import ProjectDetail, ProjectList

"""
URL patterns for portfolio projects

"""

urlpatterns = [
    url(r'^$',
        ProjectList.as_view(),
        name='portfolio_project_list'),

    url(r'^(?P<slug>[-\w]+)/$',
        ProjectDetail.as_view(),
        name='portfolio_project_detail')
]
