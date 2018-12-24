from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'general/dummy.html')

def about_us(request):
    return render(request, 'general/about_us.html')


def faq(request):
    # return HttpResponse("This is the faq part")
    # return render(request, 'expenses/dummy.html')
    return render(request, 'general/faq.html')
