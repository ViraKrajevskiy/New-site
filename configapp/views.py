from django.shortcuts import render,redirect

from .forms import NewsForm, CategoryForm
from .models import *

def index(request):
    news = News.objects.all()
    categories = Categories.objects.all()

    context = {
        "news":news,
        "categories":categories
    }
    return render(request, 'index.html', context=context)


def category_news(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Categories.objects.all()

    context = {
        "news": news,
        "categories": categories
    }
    return render(request, 'categories.html', context=context)


def new_about(request, new_id):
    news = News.objects.get(pk=new_id)

    context = {
        "news": news
    }
    return render(request, 'new_about.html', context=context)


def add_news(request):
    print(request)
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            news = News.objects.create(**form.cleaned_data)
            return redirect('home')
    else:
        form = NewsForm()
    return render(request, "add_news.html", {"form": form})

def add_categories(request):
    print(request)
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            user = Categories.objects.create(**form.cleaned_data)
            return redirect('home')
    else:
        form = CategoryForm()
    return render(request, "add_categories.html", {"form": form})