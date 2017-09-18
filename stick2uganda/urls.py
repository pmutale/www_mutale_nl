from django.conf.urls import url
from django.views.generic import TemplateView

from . import views
from .views import (
    ProjectView,
    ProjectPageView,
    AddQuestion
)

__all__ = ('urlpatterns',)

app_name = 'stick2uganda'
urlpatterns = [
    url(r'^$', ProjectView.as_view(), name='project'),
    url(r'^add-report/', views.addreport, name='add_report'),
    url(r'^add-question/', AddQuestion.as_view(), name='add_question'),
    url(r'add-findings/', views.add_findings, name='add-findings'),
    url(r'^(?P<pk>[-\w]+)$', ProjectPageView.as_view(), name='project-detail'),
]
