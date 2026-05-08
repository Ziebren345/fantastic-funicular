from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    CATEGORY_CHOICES = [
        ('planet', 'Planet Profile'),
        ('species', 'Species Database'),
        ('technology', 'Technology'),
        ('history', 'Historical Record'),
        ('threat', 'Threat Assessment'),
        ('organization', 'Organization'),
        ('event', 'Notable Event'),
        ('other', 'Other'),
    ]
    CLASSIFICATION_CHOICES = [
        ('public', 'Public'),
        ('restricted', 'Restricted'),
        ('classified', 'Classified'),
        ('top_secret', 'Top Secret'),
    ]

    title = models.CharField(max_length=300)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    classification = models.CharField(max_length=20, choices=CLASSIFICATION_CHOICES, default='restricted')
    content = models.TextField()
    summary = models.TextField(blank=True, max_length=500)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    related_factions = models.ManyToManyField('diplomacy.Faction', blank=True)
    related_planets = models.ManyToManyField('diplomacy.Planet', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return f"[{self.get_category_display()}] {self.title}"

    class Meta:
        ordering = ['-created_at']


class ArticleRevision(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='revisions')
    content = models.TextField()
    revised_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    revised_at = models.DateTimeField(auto_now_add=True)
    change_summary = models.CharField(max_length=300, blank=True)

    class Meta:
        ordering = ['-revised_at']
