from django.shortcuts import render, HttpResponse


def hello(request, nome, idade):
    return HttpResponse(f'<h1>Olá {nome} de {idade} anos!</h1>')
