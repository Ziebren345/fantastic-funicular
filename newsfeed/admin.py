from django.contrib import admin
from .models import NewsArticle


@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ['headline', 'importance', 'is_published', 'published_at', 'author_name']
    list_filter = ['importance', 'is_published']
    search_fields = ['headline', 'body', 'tags']
    actions = ['publish_articles', 'unpublish_articles']

    def publish_articles(self, request, queryset):
        queryset.update(is_published=True)
    publish_articles.short_description = "Publish selected articles"

    def unpublish_articles(self, request, queryset):
        queryset.update(is_published=False)
    unpublish_articles.short_description = "Unpublish selected articles"
