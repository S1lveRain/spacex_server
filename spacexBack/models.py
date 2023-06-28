from django.db import models

class Block(models.Model):
    head = models.CharField(max_length=255)
    center = models.CharField(max_length=255)
    bottom = models.CharField(max_length=255)
