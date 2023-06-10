from django.http import HttpResponse
from django.shortcuts import redirect, render


def index(request):

    return render(request, 'index.html', {})


def about(request):
    return HttpResponse("My name is Nikita")


def contacts(request):
    return render(request, 'contacts.html', {})


def hobbies(request):
    return HttpResponse("My hobbies")



def gallery(request):
    return HttpResponse("My gallery")


def photo(request):
    return HttpResponse("My photo")

def opros(request):
    return render(request, 'opros.html', {})

def calc(request):
    return render(request, 'calc.html', {})

def logo(request):
    return render(request, 'logo.html', {})