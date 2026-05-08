from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Article


@login_required
def article_list(request):
    category = request.GET.get('category')
    articles = Article.objects.filter(published=True)
    if category:
        articles = articles.filter(category=category)
    categories = Article.CATEGORY_CHOICES
    return render(request, 'intel/article_list.html', {
        'articles': articles,
        'categories': categories,
        'current_category': category,
    })


@login_required
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk, published=True)
    return render(request, 'intel/article_detail.html', {'article': article})
