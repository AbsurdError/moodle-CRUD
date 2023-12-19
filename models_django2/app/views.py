from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm
from django.http import HttpResponseNotFound, HttpResponseRedirect

def news_list(request):
    news = News.objects.all()
    return render(request, 'news_list.html', {'news': news})
    
def add(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsForm()
    return render(request, 'add_news.html', {'form': form})
def index(request):
    news = News.objects.all()
    return render(request, 'index.html', context={'news': news})

def news_edit(request, id):
    try:
        news = News.objects.get(id=id)

        if request.method == 'POST':
            form = NewsForm(request.POST, instance=news)
            if form.is_valid():
                form.save()
                return redirect('news_list')
        else:
            form = NewsForm(instance=news)
        return render(request, 'edit.html', {'form': form})
    except News.DoesNotExist:
        return HttpResponseNotFound('<h2>News not found</h2>')

def news_delete(request, id):
    try:
        news = News.objects.get(id=id)
        news.delete()
        return redirect('news_list')
    except News.DoesNotExist:
        return HttpResponseNotFound('<h2>News not found</h2>')
