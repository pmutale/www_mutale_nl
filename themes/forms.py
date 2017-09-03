from django import forms
from django.utils.translation import ugettext_lazy as _
from themes.utils import validate_email_address


class Subscribe(forms.Form):
    email = forms.EmailField(label=_('Email'),
                             max_length=128,
                             required=True,
                             widget=forms.EmailInput(attrs={'class': u'form-control', 'placeholder': 'email@example.com'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            validate_email_address(email)
        except:
            raise forms.ValidationError(
                _('Please provide a valid email address.'))
        return email
