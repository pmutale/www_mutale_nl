from django.conf.urls import url
from django.views.generic import TemplateView

from . import views
from .views import (
    ProjectView,
    ProjectPageView

    # AddReportView,
)

# __all__ = ('urlpatterns',)

app_name = 'stick2uganda'
urlpatterns = [
    url(r'^$', ProjectView.as_view(), name='project'),
    url(r'^add-report/', views.addreport, name='add_findings'),
    url(r'add-question/', views.addquestion, name='add-question'),
    url(r'^(?P<pk>[-\w]+)$', ProjectPageView.as_view(), name='project-detail'),
]
