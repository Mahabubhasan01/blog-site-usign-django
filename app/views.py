from django.shortcuts import render

from app.models import Fetured

# Create your views here.



def base(request):
    
    return render(request, 'core.html')


def home(request):
    return render(request, 'home.html')


def blogs(request):
    fm = Fetured.objects.all()
    print(fm)
    return render(request, 'blogs.html', {"featureds": fm})


def blog(request):
    return render(request, 'blog.html')


def login(request):
    return render(request, 'login.html')


def footer(request):
    return render(request, 'footer.html')
