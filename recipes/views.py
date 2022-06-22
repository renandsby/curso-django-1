from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'recipes/home.html', context={'name': 'Luiz otavio'})


def contato(request):
    return render(request, 'me-apague/template_temporario.html')


def sobre(request):
    return HttpResponse('sobre   3')
