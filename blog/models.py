from django.db import models
from django.utils import timezone

# Create your models here.


class Article(models.Model):
    title = models.CharField("标题", max_length=32, default="title")
    category = models.CharField("标签", max_length=20, blank=True)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    update_time = models.DateTimeField("修改时间", auto_now=True)
    content = models.TextField("内容", blank=True, null=True)

    def __str__(self):
        return self.title
