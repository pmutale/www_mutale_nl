from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from stick2uganda.models import Project


class ProjectView(TemplateView):
    """
    Our projects in Uganda

    """
    model = Project
    template_name = 'stick2uganda/project.html'

    def get_data(self, context):
        return list(
            self.model.objects.all()
                .only('name',
                      'location')
                .values('name',
                        'location')
        )


class IndexView(TemplateView):
    template_name = 'stick2uganda/index.html'


