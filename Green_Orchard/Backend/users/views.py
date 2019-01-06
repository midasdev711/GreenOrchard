from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'name': 'Alex Rogers',
        'banks': ['Wells Fargo', 'Discover', 'Capital One', 'Bank of America']
    }
    return render(request, 'users/user_profile.html', context)
    # return render(request, 'users/dummy.html')

def login(request):
    return render(request, 'users/dummy.html')
    # return render(request, 'users/login.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Successfully registered!')
            return redirect('profile')
    else:
        form = UserCreationForm()
    context = {
        'title': 'Register',
        'form': form,
    }
    # return render(request, 'users/dummy.html')
    return render(request, 'users/register.html', context)

def edit_profile(request):
    return render(request, 'users/dummy.html')
