from django.forms import ModelForm
from django import forms
from .models import Physician


class PhysicianSignupForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    email_id = forms.EmailField(required=True)

    class Meta:
        # write the name of models for which the form is made
        model = Physician

        # Custom fields
        fields = ["email_id", "password", "first_name", "last_name"]

        # this function will be used for the validation

    def clean(self):
        # data from the form is fetched using super function
        super(PhysicianSignupForm, self).clean()

        # extract the username and text field from the data
        email_id = self.cleaned_data.get('email_id')
        password = self.cleaned_data.get('password')
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')

        # conditions to be met for the password length

        if len(password) < 3:
            self._errors['password'] = self.error_class([
                'Post Should Contain minimum 3 characters'])

            # return any errors if found
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
