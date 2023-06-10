import requests
from django.shortcuts import redirect, render


def index(request):

    responce = requests.get('https://swapi.dev/api/')

    return render(request, 'api.html', {"responce": responce.json().items()})
