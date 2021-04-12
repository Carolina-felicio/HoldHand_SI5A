from django import forms
from django.contrib.auth.views import PasswordResetForm
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox, ReCaptchaV2Invisible, ReCaptchaV3
from django.contrib.auth.models import User
from .models import UserProfile
from dataclasses import dataclass, fields
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control border border-dark rounded text-dark', 'required': True}),
            'last_name': forms.TextInput(attrs={'class': 'form-control border border-dark rounded text-dark', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control border border-dark rounded text-dark', 'required': True}),
        }

        labels = {
            'first_name': "Name",
            'last_name': "Surname",
            'email': "Email",
        }


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        exclude = ('username', '')

        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control phone-ddd-mask border border-dark rounded text-dark'}),
            'cell_phone': forms.TextInput(attrs={'class': 'form-control border border-dark rounded text-dark', 'data-mask': '(99)99999-9999'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control border border-dark rounded text-dark'}),
            'address': forms.TextInput(attrs={'class': 'form-control border border-dark rounded text-dark'}),
            'district': forms.TextInput(attrs={'class': 'form-control border border-dark rounded text-dark'}),
            'number': forms.TextInput(attrs={'class': 'form-control border border-dark rounded text-dark'}),
            'complement': forms.TextInput(attrs={'class': 'form-control border border-dark rounded text-dark'}),
            'city': forms.TextInput(attrs={'class': 'form-control border border-dark rounded text-dark'}),
            'uf': forms.TextInput(attrs={'class': 'form-control border border-dark rounded text-dark'})
        }

        labels = {
            'phone': 'Phone',
            'cell_phone': 'Cell phone',
            'zip_code': 'Zip Code',
            'address': 'Address',
            'district': 'District',
            'number': 'Number',
            'complement': 'Complement',
            'city': 'City',
            'uf': 'Uf'
        }


class UserDeleteForm(forms.ModelForm):

    class Meta:
        model = User
        fields = []   #Form has only submit button.  Empty "fields" list still necessary, though.


class PythonProResetForm(PasswordResetForm):
    captcha = ReCaptchaField(widget=ReCaptchaV3)

# The ReCaptchaV2Invisible widget
# ignores the "data-size" attribute in favor of 'data-size="invisible"'


class ExampleForm(forms.Form):
    captcha = ReCaptchaField(widget=ReCaptchaWidget())

