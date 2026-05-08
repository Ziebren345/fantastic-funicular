from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import NewsArticle


@login_required
def news_list(request):
    articles = NewsArticle.objects.filter(is_published=True)
    importance = request.GET.get('importance')
    if importance:
        articles = articles.filter(importance=importance)
    return render(request, 'newsfeed/news_list.html', {'articles': articles})


@login_required
def news_detail(request, pk):
    article = get_object_or_404(NewsArticle, pk=pk, is_published=True)
    return render(request, 'newsfeed/news_detail.html', {'article': article})
