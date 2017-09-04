from django.conf.urls import url

from .views import (
    ProjectView,
    IndexView,
    # PublisherList,
)

__all__ = ('urlpatterns',)


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^project/$', ProjectView.as_view(), name='projects'),
    # Publishers list
    # url(r'^add-report/$', PublisherList.as_view(), name='exercises.publishers'),

]