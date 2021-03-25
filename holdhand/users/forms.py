from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control border border-dark rounded text-dark required'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control border border-dark rounded text-dark'}),
            'email': forms.EmailInput(attrs={'class': 'form-control border border-dark rounded text-dark'}),
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
            'cell_phone': forms.TextInput(attrs={'class': 'form-control cel-sp-mask border border-dark rounded text-dark'}),
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
