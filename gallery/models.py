from django.db import models

# Create your models here.
# 创建app，在控制台里面创建
# 创建app，使用 python manage.py startapp

class Gallery(models.Model):
		descrption = models.CharField(default='这里是默认描述', max_length=100)
		gimage = models.ImageField(default='default.png', upload_to='gimages/')
		gtitle = models.CharField(default='作品标题', max_length=50)

		def __str__(self):
			return self.gtitle
    