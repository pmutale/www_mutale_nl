from django.db.models import Count
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from stick2uganda.models import Project


class ProjectView(ListView):
    """
    Our projects in Uganda
    """
    model = Project
    template_name = 'stick2uganda/project.html'

    def get_queryset(self):
        return self.model.objects.all().annotate(number_of_reports=Count('report'),
                                                 number_of_contacts=Count('contact'))
