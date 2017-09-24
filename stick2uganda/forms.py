from django.forms import ModelForm, Select, Textarea, inlineformset_factory, \
    TextInput, DateInput, modelformset_factory, ImageField
from stick2uganda.models import Project, Report, Question
from django.utils.translation import gettext as _


class AddReportForm(ModelForm):
    class Meta:
        model = Report
        fields = '__all__'


class AddQuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = 'number', 'question', 'project'
        widgets = {
            'number': TextInput(attrs={'class': 'form-control'}),
            'question': TextInput(attrs={'class': 'form-control'}),
            'project': Select(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(AddQuestionForm, self).__init__(*args, **kwargs)
        self.fields['project'].empty_label = _('Please Select a Project from the list below')


QuestionFormset = modelformset_factory(Question, extra=0, fields=('number', 'project', 'question', 'findings', 'image'),
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

