from django.shortcuts import render
from django.http import HttpResponse

def blog(request):

    context = {
            'text': 'Olá little blog',
            'title': 'Essa é uma página de exemplo - '
        }    
    return render(
        request,
        'blog/index.html',
        context,
    )


def exemplo(request):

    context = {
            'text': 'Estamos na home'
        }
    return render(
        request,
        'blog/exemplo.html',
        context,
    )