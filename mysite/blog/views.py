from django.shortcuts import render
from .models import Post
from django.http import Http404
from django.shortcuts import render, get_object_or_404


def post_list(request):
    posts = Post.published.all()  # Тут мы извлекаем все значения со статусом Published
    return render(request, 'post/list.html', {'posts': posts})


def post_detail(request, id):
    # try:
    #     posts = Post.published.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404('Not Post found')
    posts = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)

    return render(request, 'post/detail.html', {'posts': posts})

