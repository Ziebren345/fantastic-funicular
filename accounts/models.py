from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('gm', 'Game Master (Tribunii)'),
        ('player', 'Keleres Agent'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='player')
    callsign = models.CharField(max_length=100, blank=True, help_text="In-universe codename")
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)

    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username} ({self.get_callsign()})"

    def get_callsign(self):
        return self.callsign or self.user.username

    def is_gm(self):
        return self.role == 'gm'

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'
