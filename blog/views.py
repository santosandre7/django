from django.shortcuts import render
from blog.data import posts
from django.http import HttpRequest, Http404

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

def post(request, post_id):

    found_post = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break

    if found_post is None:
        raise Http404('Post não existe')

    context = {
            # 'text': 'Olá little blog',
            # 'title': 'Essa é uma página de exemplo - ',
            'post': found_post,
            'title': found_post['title'] + ' - '
        }    
    return render(
        request,
        'blog/post.html',
        context,
    )