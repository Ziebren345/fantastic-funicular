from django.contrib import admin
from .models import Article, ArticleRevision


class ArticleRevisionInline(admin.TabularInline):
    model = ArticleRevision
    extra = 0
    readonly_fields = ['content', 'revised_by', 'revised_at', 'change_summary']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'classification', 'published', 'created_at']
    list_filter = ['category', 'classification', 'published']
    search_fields = ['title', 'content', 'summary']
    filter_horizontal = ['related_factions', 'related_planets']
    inlines = [ArticleRevisionInline]
