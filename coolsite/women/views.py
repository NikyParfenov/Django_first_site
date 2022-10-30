from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *

menu = ['About', 'Add article', 'Contact', 'Sign in']


# Create your views here.
def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'posts': posts, 'menu': menu, 'title': 'Main page'})


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'About'})


def categories(request, catid):
    if request.GET:
        print(request.GET)
    if request.POST:
        print(request.POST)
    return HttpResponse(f'<h1>Статья по категориям</h1><p>{catid}</p>')


def archive(request, year):
    if int(year) > 2022:
        raise Http404
    if int(year) == 2022:
        return redirect('home', permanent=True)
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
