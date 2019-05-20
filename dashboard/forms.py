# Django
from django import forms
# Django Translation
from django.utils.translation import gettext as _
from django.utils.translation import ugettext_lazy as _l

class ContactForm(forms.Form):
    fullname = forms.CharField(label=_l('Full name'), max_length='256', required=True)
    email = forms.EmailField(label=_l('Email'), required=True)
    topic = forms.CharField(label=_l('Topic'), max_length=256, required=True)
    question = forms.CharField(label=_l('Question'), max_length=5000, required=True, widget=forms.Textarea)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fullname'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['topic'].widget.attrs.update({'class': 'form-control'})
        self.fields['question'].widget.attrs.update({'class': 'form-control'})
    
    def clean(self):
        name = self.cleaned_data.get("fullname")
        email = self.cleaned_data.get("email")
        topic = self.cleaned_data.get("topic")
        question = self.cleaned_data.get("question")
        if name == '' or name is None:
            raise forms.ValidationError(_l("You must write your full name"))