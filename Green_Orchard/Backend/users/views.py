from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

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
        form = UserRegisterForm(request.POST)
        form.save() # Also hashes password for security
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} has successfully registered!')
            return redirect('users:main_profile')
    else:
        form = UserRegisterForm()
    context = {
        'title': 'Register',
        'form': form,
    }
    # return render(request, 'users/dummy.html')
    return render(request, 'users/register.html', context)

def edit_profile(request):
    return render(request, 'users/dummy.html')
