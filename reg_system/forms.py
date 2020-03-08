import re

from django.forms import ModelForm
from django import forms
from .models import Physician, Patient


class PhysicianSignupForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    re_password = forms.CharField(widget=forms.PasswordInput)
    email_id = forms.EmailField(required=True)

    class Meta:
        # write the name of models for which the form is made
        model = Physician

        # Custom fields
        fields = ["first_name", "last_name", "email_id", "password", "re_password"]

        # this function will be used for the validation

    def clean(self):
        # data from the form is fetched using super function
        super(PhysicianSignupForm, self).clean()

        # extract the username and text field from the data
        email_id = self.cleaned_data.get('email_id')
        password = self.cleaned_data.get('password')
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        re_password = self.cleaned_data.get("re_password")

        # conditions to be met for the password length

        if not re.findall('[a-zA-Z][a-zA-Z ]*[a-zA-Z]$', first_name):
            self._errors['first_name'] = self.error_class([
                "First name should only contain letters and spaces."])

        if not re.findall('[a-zA-Z][a-zA-Z ]*[a-zA-Z]$', last_name):
            self._errors['last_name'] = self.error_class([
                "Last name should only contain letters and spaces."])

        if len(password) < 6:
            self._errors['password'] = self.error_class([
                'Password Should Contain minimum 6 characters'])

        if not re.findall('\d', password):
            self._errors['password'] = self.error_class([
                "The password must contain at least 1 digit, 0-9."])

        if not re.findall('[A-Z]', password):
            self._errors['password'] = self.error_class([
                "The password must contain at least one Uppercase Character."])

        if not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', password):
            self._errors['password'] = self.error_class([
                "The password must contain at least 1 special character."])

        if not password == re_password:
            self._errors['re_password'] = self.error_class([
                "The password does not match "])

        return self.cleaned_data


class PhysicianLoginForm(forms.Form):
    email_id = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        # Custom fields
        fields = ["email_id", "password"]

        # this function will be used for the validation

    def clean(self):
        # data from the form is fetched using super function
        super(PhysicianLoginForm, self).clean()

        # extract the username and text field from the data
        email_id = self.cleaned_data.get('email_id')
        password = self.cleaned_data.get('password')

        return self.cleaned_data


class PatientSignupForm(ModelForm):
    email_id = forms.EmailField(required=True)

    class Meta:
        # write the name of models for which the form is made
        model = Patient

        # Custom fields
        fields = ["first_name", "last_name", "email_id"]

        # this function will be used for the validation

    def clean(self):
        # data from the form is fetched using super function
        super(PatientSignupForm, self).clean()

        # extract the username and text field from the data
        email_id = self.cleaned_data.get('email_id')
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')

        if not re.findall('[a-zA-Z][a-zA-Z ]*[a-zA-Z]$', first_name):
            self._errors['first_name'] = self.error_class([
                "First name should only contain letters and spaces."])

        if not re.findall('[a-zA-Z][a-zA-Z ]*[a-zA-Z]$', last_name):
            self._errors['last_name'] = self.error_class([
                "Last name should only contain letters and spaces."])

        return self.cleaned_data
