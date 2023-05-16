from django.shortcuts import render
from django.http import HttpResponse

#view index
def index(request):
    return HttpResponse("Olá, seja bem vindo a enquete")

def sobre(request):
    return HttpResponse("Este é um app de enquete")