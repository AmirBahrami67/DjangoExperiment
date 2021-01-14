from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
    print(request)
    print(args)
    print(kwargs)
    return render(request, "home.html", {'name': request.user})


def contact_view(request, *args, **kwargs):
    print(args)
    print(kwargs)
    return render(request, "contact.html", {'name': request.user})

def about_view(request, *args, **kwargs):
    print(args)
    print(kwargs)
    return render(request, "about.html", {'name': request.user})
