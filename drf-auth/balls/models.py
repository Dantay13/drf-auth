from django.contrib.auth import get_user_model
from django.db import models


class Ball(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    type = models.CharField(max_length=64)
    brand = models.CharField(max_length=64)
    color = models.CharField(max_length=32)
    material = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.type
