from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RegForm

# Create your views here.
def register(request):
    form = RegForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            username = form.data.get('username')
            messages.success(request, f'Account created successfully for {username}' )
            return redirect('login')

    return render(request, 'register.html', {'form': form})