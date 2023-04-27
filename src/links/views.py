from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
    global dj_context
    dj_context = {
        "my_text": "This is about us",
        "my_number": 1234,
        "my_list": [324, 4356, 35367, 4535, 12134]
    }
    return render(request, "about.html", dj_context)


def social_view(request, *args, **kwargs):
    return render(request, "social.html", dj_context)
