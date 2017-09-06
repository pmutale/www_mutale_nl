from django.forms import ModelForm, forms, formset_factory, modelform_factory, Select, Textarea, inlineformset_factory, \
    TextInput, DateInput, modelformset_factory
from stick2uganda.models import Project, Report, Question


class AddReportForm(ModelForm):
    class Meta:
        model = Report
        fields = '__all__'


QuestionFormset = modelformset_factory(Question, extra=0, fields=('number', 'project', 'question', 'findings'),
                                       widgets={
                                           'number': TextInput(attrs={'class': 'form-control',
                                                                      'readonly': 'readonly'}),
                                           'question': TextInput(attrs={'class': 'form-control',
                                                                        'readonly': 'readonly'}),
                                           'project': Select(attrs={'class': 'form-control-static',
                                                                    'readonly': 'readonly'}),
                                           'findings': Textarea(attrs={'class': 'form-control'}),
                                       })

ReportFormSet = modelformset_factory(Report, fields=('version', 'completed', 'question'),
                                     widgets={'version': TextInput(attrs={'class': 'form-control'}),
                                              'completed': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
                                              'question': Select(attrs={'class': 'form-control'})}
                                     )

