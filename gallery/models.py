from django.db import models

# Create your models here.
class Gallery(models.Model):
		descrption = models.CharField(max_length=50)
    