from django.db import models
from django.contrib.auth.models import User
from personnel.models import PersonnelFile


class GearRequest(models.Model):
    URGENCY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending Review'),
        ('approved', 'Approved'),
        ('denied', 'Denied'),
        ('fulfilled', 'Fulfilled'),
    ]

    requester = models.ForeignKey(PersonnelFile, on_delete=models.CASCADE, related_name='gear_requests')
    item_name = models.CharField(max_length=200)
    item_type = models.CharField(max_length=100, blank=True, help_text="Weapon, Armor, Gear, Vehicle, etc.")
    quantity = models.PositiveSmallIntegerField(default=1)
    urgency = models.CharField(max_length=20, choices=URGENCY_CHOICES, default='medium')
    justification = models.TextField(help_text="Why is this needed for your mission?")

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    reviewed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='gear_reviews')
    review_comment = models.TextField(blank=True)
    reviewed_at = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.requester.name} - {self.item_name} x{self.quantity}"

    class Meta:
        ordering = ['-created_at']
