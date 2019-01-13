from django.db import models

# Create your models here.
# 创建app，在控制台里面创建
# 创建app，使用 python manage.py startapp

class Gallery(models.Model):
		descrption = models.CharField(max_length=50)
    