from django.db.models import Count
from django.forms import modelformset_factory, TextInput, DateInput, Textarea
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from . import forms
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from stick2uganda.models import Report, Question, Project


class ProjectView(ListView):
    """
    Our projects in Uganda
    """
    model = Project
    template_name = 'stick2uganda/project.html'

    def get_queryset(self):
        return self.model.objects.all().annotate(number_of_reports=Count('projects_report'),
                                                 number_of_contacts=Count('projects_contact'))


def addreport(request):
    ReportFormSet = forms.ReportFormSet
    if request.method == 'POST':
        formset = ReportFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return redirect('/project')
    else:
        formset = ReportFormSet()
    return render(request, 'stick2uganda/addquestion.html', {'formset': formset})


def addquestion(request):
    QuestionFormset = forms.QuestionFormset

    if request.method == 'POST':
        formset = QuestionFormset(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return redirect('/project')
    else:
        formset = QuestionFormset()
    return render(request, 'stick2uganda/addfindings.html', {'formset': formset})


class ProjectPageView(DetailView):
    template_name = 'stick2uganda/project/project_page.html'
    model = Project

    def get_context_data(self, **kwargs):
        context = super(ProjectPageView, self).get_context_data(**kwargs)
        context['project'] = self.model.objects.all()
        return context
