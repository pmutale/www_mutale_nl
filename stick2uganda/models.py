from __future__ import unicode_literals

from ckeditor.fields import RichTextField
from filer.fields.image import FilerImageField
from cms.models import CMSPlugin
from django.utils.translation import ugettext_lazy as _

from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=128, null=False)
    image = FilerImageField(null=True, blank=True)
    project_summary = RichTextField(null=True, blank=True)
    location = models.CharField(max_length=128, null=False)
    start_implementation = models.DateField(null=True, blank=True)
    end_implementation = models.DateField(null=True, blank=True)

    def __str__(self):
        return '{} in {}'.format(self.name, self.location)


class ContactPerson(models.Model):
    name = models.CharField(max_length=128)
    telephone = models.CharField(max_length=128, null=True, blank=True)
    email = models.EmailField(max_length=128, null=True, blank=True)
    project = models.ForeignKey('Project', on_delete=models.CASCADE, null=True, related_name='projects_contact')

    def __str__(self):
        return '{} - {}'.format(self.name, self.email)


class Report(models.Model):
    version = models.CharField(max_length=128, null=True, blank=True,
                               help_text=(_('Use numbers <small>e.g</small> A or B')))
    completed = models.DateField(null=True, blank=True)
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='questions')
    project = models.ForeignKey('Project', on_delete=models.CASCADE, null=True, related_name='projects_report')

    class Meta:
        permissions = (
            ('can_add_report', 'Can add Rreport'),
            ('can_edit_report', 'Can edit Report')
        )

    def __str__(self):
        return '{} completed on {}'.format(self.version, self.completed)


class Question(models.Model):
    number = models.IntegerField(null=True, blank=True, help_text=(_('Use numbers <small>e.g</small> 1, 2 or 3')))
    question = models.CharField(max_length=128, null=True, blank=True)
    findings = RichTextField(null=True, blank=True)
    image = models.ImageField(max_length=128000, null=True, blank=True, upload_to='media/project')
    project = models.ForeignKey('Project', on_delete=models.CASCADE, null=True, related_name='projects_question')

    class Meta:
        permissions = (
            ('can_add_question', 'Can add Question'),
            ('can_edit_question', 'Can edit Question')
        )

    def __str__(self):
        return '{} for {}'.format(self.number, self.project)


class Stick2UgandaPlugin(CMSPlugin):
    info = RichTextField(null=True, blank=True)
    intro_small = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return self.stick2uganda.name


class S2UImagePlugin(CMSPlugin):
    image = FilerImageField(blank=True, null=True)
    title = models.CharField(max_length=128, blank=True, null=True)

