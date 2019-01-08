from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'css_file': 'general/index.css',
    }
    return render(request, 'general/index.html')

def about_us(request):
    context = {
        'css_file': 'general/about_us.css',
    }
    return render(request, 'general/about_us.html', context)

def faq(request):
    context = {
        'css_file': 'general/faq.css',
    }
    # return HttpResponse("This is the faq part")
    # return render(request, 'expenses/dummy.html')
    return render(request, 'general/faq.html', context)
