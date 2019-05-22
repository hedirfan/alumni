from django import forms
from .models import Identita
from django.forms import ModelForm

class IdentitaForm(forms.ModelForm):
    class Meta:
        model = Identita
        fields = ['username', 'password', 'email', 'fullname',
                  'address', 'phone_number', 'year', 'job']
