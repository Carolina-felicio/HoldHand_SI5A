from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control border border-dark rounded text-dark'}),
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
        exclude = ('user', '')

        widgets = {
            'segment': forms.TextInput(attrs={'class': 'form-control border border-dark rounded text-dark'}),
            'store_name': forms.TextInput(attrs={'class': 'form-control border border-dark rounded text-dark'}),
            'address': forms.TextInput(attrs={'class': 'form-control border border-dark rounded text-dark'}),
            'payment_method': forms.TextInput(attrs={'class': 'form-control border border-dark rounded text-dark'}),
        }

        labels = {
            'segment': 'Segment',
            'store_name': 'Store Name',
            'address': 'Address',
            'payment_method': 'Payment Method'
        }
