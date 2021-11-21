from django import forms
from django.forms.fields import CharField, EmailField


class FormName(forms.Form):
    name = forms.CharField(max_length=264)
    email = forms.EmailField(max_length=264)
    text = forms.CharField(widget=forms.Textarea)
