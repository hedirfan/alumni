from django.shortcuts import render, redirect
from mahasantri.models import Identita
from mahasantri.forms import IdentitaForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = IdentitaForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('homepage')
    else:
        form = IdentitaForm()
    return render(request, 'mahasantri/register.html', {'form': form})
