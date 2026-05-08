from django.db import models
from django.contrib.auth.models import User


class NewsArticle(models.Model):
    IMPORTANCE_CHOICES = [
        ('minor', 'Minor'),
        ('notable', 'Notable'),
        ('major', 'Major'),
        ('breaking', 'BREAKING'),
    ]

    headline = models.CharField(max_length=300)
    subheadline = models.CharField(max_length=500, blank=True)
    body = models.TextField()
    author_name = models.CharField(max_length=200, blank=True, help_text="In-universe journalist name")
    importance = models.CharField(max_length=20, choices=IMPORTANCE_CHOICES, default='notable')
    tags = models.CharField(max_length=500, blank=True, help_text="Comma-separated tags")
    published_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    image = models.ImageField(upload_to='news/', blank=True)
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"[{self.get_importance_display()}] {self.headline}"

    class Meta:
        ordering = ['-published_at']
        verbose_name = 'News Article'
        verbose_name_plural = 'News Articles'
