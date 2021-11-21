from django import forms
from django.forms.fields import CharField, EmailField
from django.core import validators


# def check_for_z(value):
#     if value[0].lower() != "z":
#         raise forms.ValidationError("Name Needs to Start With Z")


class FormName(forms.Form):
    # name = forms.CharField(validators=[check_for_z])
    name = forms.CharField()
    email = forms.EmailField(max_length=264)
    verify_email = forms.EmailField(label="Enter your email again:")
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(
        required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)]
    )

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data["email"]
        vemail = all_clean_data["verify_email"]

        if email != vemail:
            raise forms.ValidationError("Make sure emails match!")
