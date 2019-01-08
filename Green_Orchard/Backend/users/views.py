from django.shortcuts import render

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
    # return render(request, 'users/dummy.html')
    return render(request, 'users/register.html', {'title': 'Register'})

def edit_profile(request):
    return render(request, 'users/dummy.html')
