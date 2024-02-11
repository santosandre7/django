from django.shortcuts import render
from blog.data import posts

def blog(request):

    context = {
            'text': 'Olá little blog',
            'title': 'Essa é uma página de exemplo - ',
            'posts': posts
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