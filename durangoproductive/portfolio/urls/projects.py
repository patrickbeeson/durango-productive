from django.conf.urls import url

from portfolio import views

"""
URL patterns for portfolio projects

"""

urlpatterns = [
    url(r'^$',
        views.ProjectList.as_view(),
        name='portfolio_project_list'),

    url(r'^(?P<slug>[-\w]+)/$',
        views.ProjectDetail.as_view(),
        name='portfolio_project_detail')
]
