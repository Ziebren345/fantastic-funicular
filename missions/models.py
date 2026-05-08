from django.db import models
from django.contrib.auth.models import User
from personnel.models import PersonnelFile


class Mission(models.Model):
    CLASSIFICATION_CHOICES = [
        ('public', 'Public'),
        ('restricted', 'Restricted'),
        ('classified', 'Classified'),
        ('top_secret', 'Top Secret'),
    ]
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('complete', 'Completed'),
        ('failed', 'Failed'),
        ('aborted', 'Aborted'),
    ]

    title = models.CharField(max_length=200)
    codename = models.CharField(max_length=100, blank=True, help_text="Classified operation codename")
    classification = models.CharField(max_length=20, choices=CLASSIFICATION_CHOICES, default='classified')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')

    briefing = models.TextField(blank=True)
    debrief = models.TextField(blank=True, help_text="Post-mission report")

    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='authored_missions')
    assigned_personnel = models.ManyToManyField(PersonnelFile, blank=True, related_name='missions')

    location = models.CharField(max_length=200, blank=True, help_text="Planet or sector")
    threat_level = models.CharField(max_length=50, blank=True, help_text="Low, Medium, High, Critical")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"[{self.status.upper()}] {self.codename or self.title}"

    class Meta:
        ordering = ['-created_at']


class Objective(models.Model):
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE, related_name='objectives')
    order = models.PositiveSmallIntegerField(default=0)
    description = models.TextField()
    is_primary = models.BooleanField(default=True)
    is_complete = models.BooleanField(default=False)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.mission.codename or self.mission.title} - Obj {self.order}"

    class Meta:
        ordering = ['mission', 'order']
