from django.db import models
from django.contrib.auth import get_user_model
from .utils import base62_encode

User = get_user_model()


class URL(models.Model):
    long_url = models.CharField(max_length=200)
    short_url = models.CharField(max_length=7, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.id:
            super().save(*args, **kwargs)
        
        if not self.short_url:
            self.short_url = base62_encode(self.id)
            super().save(*args, **kwargs)

    def __str__(self):
        return self.url
