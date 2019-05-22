from django.db import models
from django.forms import ModelForm


class Identita(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    email = models.EmailField(max_length=70)
    fullname = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    year = models.DateField()
    job = models.CharField(max_length=10)

    def __str__(self):
        return self.fullname


class IdentitaForm(ModelForm):
    class Meta:
        model = Identita
        fields = ['username', 'password', 'email', 'fullname',
                  'address', 'phone_number', 'year', 'job']
