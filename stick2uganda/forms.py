from django.forms import ModelForm, Select, Textarea, inlineformset_factory, \
    TextInput, DateInput, modelformset_factory, ImageField, BaseModelFormSet
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


class BaseQuestionFormset(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        super(BaseQuestionFormset, self).__init__(*args, **kwargs)
        self.queryset = Question.objects.select_related('project')\
            .filter(findings__contains='Add Your Findings here')


QuestionFormset = modelformset_factory(Question,
                                       fields=('number', 'project', 'question', 'findings', 'image'),
                                       extra=0,
                                       widgets={
                                           'number': TextInput(attrs={'class': 'form-control',
                                                                      'readonly': 'readonly'}),
                                           'question': TextInput(attrs={'class': 'form-control',
                                                                        'readonly': 'readonly'}),
                                           'project': Select(attrs={'class': 'form-control-static',
                                                                    'readonly': 'readonly'}),
                                           'findings': Textarea(attrs={'class': 'form-control'}),
                                       },
                                       formset=BaseQuestionFormset)


class BaseReportFormset(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        super(BaseReportFormset, self).__init__(*args, **kwargs)
        self.queryset = Report.objects.filter(version__isnull=True, question__isnull=True).\
            select_related('question')


ReportFormSet = modelformset_factory(Report,
                                     fields=('version', 'completed', 'question'),
                                     extra=1,
                                     widgets={'version': TextInput(attrs={'class': 'form-control'}),
                                              'completed': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
                                              'question': Select(attrs={'class': 'form-control'})
                                              },
                                     formset=BaseReportFormset
                                     )

