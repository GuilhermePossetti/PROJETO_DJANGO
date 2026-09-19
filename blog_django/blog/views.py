from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def pagina_inicial(request):
    return HttpResponse("texto que você quiser mostrar")

