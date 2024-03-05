from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

# Create your views here.

def home_view(request:HttpRequest):


    return render(request, "main/home.html")

def properties(request:HttpRequest):

    return render(request, "main/properties.html")

def home(request):
    properties = [
        {"title": "Villa Modern in Malqa", "image": "villa1.jpg"},
        {"title": "Great home for you in Rimal", "image": "villa2.jpg"},
        {"title": "Villa with 8 bedrooms in Swedey", "image": "villa3.jpg"},
        {"title": "Amazing Villa in Hitten", "image": "villa4.jpg"},
    ]
    return render(request, "main/Properties.html", {'properties': properties})
def explore_properties(request):
    pass
def mode_dark(request:HttpRequest):

    response = redirect("main:home_view")
    response.set_cookie("Dark_mode", "True", max_age=60*60*24*7)

    return response


def mode_light(request:HttpRequest):

    response = redirect("main:home_view")
    response.set_cookie("light_mode", "False")

    return response