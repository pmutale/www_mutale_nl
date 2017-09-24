from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator

from stick2uganda.mixins import ActiveOnlyMixin
from . import forms
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.contrib.auth.decorators import (login_required,
                                            permission_required,
                                            user_passes_test)
from stick2uganda.models import Report, Question, Project


def group_required(*group_names):
    """
    Requires user membership in at least one of the groups passed in.
    """

    def in_groups(user):
        if user.is_authenticated():
            if bool(user.groups.filter(name__in=group_names)) | user.is_active:
                return True
        return False
    return user_passes_test(in_groups)


class ProjectView(ActiveOnlyMixin, ListView):
    """
    Our projects in Uganda
    """
    model = Project
    template_name = 'stick2uganda/project/project.html'
    permission_required = ('report.can_add_report', 'report.can_edit_report', 'can_add_question', 'can_edit_question')

    def get_queryset(self):
        return self.model.objects.all().prefetch_related('projects_report',
                                                         'projects_contact')


class AddQuestion(ActiveOnlyMixin, CreateView):
    model = Question
    template_name = 'stick2uganda/addquestion.html'
    form_class = forms.AddQuestionForm
    success_url = '/project/add-findings'
    permission_required('report.can_add_report', 'report.can_edit_report', 'can_add_question')


class ProjectPageView(ActiveOnlyMixin, DetailView):
    template_name = 'stick2uganda/project/project_page.html'
    model = Project
    permission_required = ('report.can_add_report', 'report.can_edit_report', 'can_add_question', 'can_edit_question')

    def get_context_data(self, **kwargs):
        context = super(ProjectPageView, self).get_context_data(**kwargs)
        context['project'] = self.model.objects.all()
        return context


@login_required
@group_required('stick2uganda')
@permission_required('report.can_add_report')
def addreport(request):
    ReportFormSet = forms.ReportFormSet
    if request.method == 'POST':
        formset = ReportFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return redirect('/project')
    else:
        formset = ReportFormSet()
    return render(request, 'stick2uganda/addreport.html', {'formset': formset})


@login_required
@group_required('stick2uganda')
# @permission_required('question.can_add_question')
def add_findings(request):
    QuestionFormset = forms.QuestionFormset
    if request.method == 'POST':
        formset = QuestionFormset(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return redirect('/project')
            # return reverse('stick2uganda:project')

    else:
        formset = QuestionFormset()
    return render(request, 'stick2uganda/addfindings.html', {'formset': formset})




