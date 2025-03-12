from django.shortcuts import render, redirect, get_object_or_404

from .forms import NewsFrom, CategoryForm, NewsAdd
from .models import *



def news_list(request):
    query = request.GET.get('q')
    if query:
        news = News.objects.filter(title__icontains=query)
    else:
        news = News.objects.all()

    return render(request, 'index.html', {'news': news})

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
    newses = News.objects.get(pk=new_id)

    context = {
        "new": newses
    }
    return render(request, 'new_about.html', context=context)


def add_news(request):
    print(request)
    if request.method == "POST":
        form = NewsFrom(request.POST)
        if form.is_valid():
            news = News.objects.create(**form.cleaned_data)
            return redirect('home')
    else:
        form = NewsFrom()
    return render(request, "add_news.html", {"form": form})


def add_categories(request):
    print(request)
    if request.method == "POST":
        form = (request.POST)
        if form.is_valid():
            user = Categories.objects.create(**form.cleaned_data)
            return redirect('home')
    else:
        form = CategoryForm()
    return render(request, "add_categories.html", {"form": form})



def add_news(request):
    if request.method == 'POST':
        form = NewsAdd(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            news = News.objects.create(**form.cleaned_data)
            news = form.save()
            return redirect(news)
    else:
        form = NewsFrom
    return render(request,'news/add_news.html',{'form':form})


def update_new(request, new_id):
    new = get_object_or_404(News, id = new_id)
    if request.method == 'POST':
        form = NewsFrom(request.POST, isinstance=new)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewsFrom(instance = new )
    return render(request,'update_now.html',{'form':form})



