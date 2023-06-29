from .models import Profile
from django.forms import ModelForm, TextInput, NumberInput, ImageField
from django import forms


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'age']
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'placeholder': "enter name",
            }),
            'age': NumberInput(attrs={
                'class': "form-control",
                'placeholder': "enter age",
            })
        }
