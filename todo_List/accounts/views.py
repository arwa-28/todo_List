from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib import messages


# Create your views here.
def welcome(request):
    return render(request, 'home/welcome.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
        else:
            messages.error(request, 'Invalid form data. Please correct the errors.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
