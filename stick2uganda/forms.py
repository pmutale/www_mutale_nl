from django.forms import ModelForm

from stick2uganda.models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'


