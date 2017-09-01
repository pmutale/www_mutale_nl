from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin
from django.db import models
from ckeditor.fields import RichTextField


class Contact(CMSPlugin):
    number = models.CharField(max_length=128)
    email = models.EmailField()
    text = RichTextField(null=True, blank=True, verbose_name=_('First Line Text'),
                         help_text='First line text')


class ComingSoon(CMSPlugin):
    email = models.EmailField()
    page_heading = models.CharField(max_length=128)
    description = RichTextField(null=True, blank=True, verbose_name=_('First Line Text'),
                                help_text='First line text')

