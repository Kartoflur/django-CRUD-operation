from django.db import models

class foodProducts(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)