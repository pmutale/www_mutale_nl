from django.conf.urls import url

from . import views
from .views import (
    ProjectView,
)

# __all__ = ('urlpatterns',)

app_name = 'stick2uganda'

urlpatterns = [
    url(r'^$', ProjectView.as_view(), name='project'),

]