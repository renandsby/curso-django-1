from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return HttpResponse('HOME   2')


def contato(request):
    return HttpResponse('contato   2')


def sobre(request):
    return HttpResponse('sobre   3')
