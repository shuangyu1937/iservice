__author__ = 'zouwei'
from django.db import models


class MessageStack(models.Model):
    id = models.AutoField()
    title = models.CharField(verbose_name="标题", max_length=100)
    summary = models.CharField(verbose_name="摘要", max_length=300)
    author = models.DateTimeField(verbose_name="作者", max_length=50)
    post_date = models.DateTimeField(verbose_name="消息时间")
    url = models.CharField(verbose_name="地址", max_length=300)
    source = models.CharField(verbose_name="来源", max_length=100)


class UserReadMessage(models.Model):
    id = models.AutoField()
    user_name = models.CharField(verbose_name="用户名", max_length=20)
    message_id = models.ForeignKey(MessageStack, verbose_name="已读消息")


class ServiceKey(models.Model):
    id = models.AutoField()
    com = models.CharField(verbose_name="公司", max_length=50)
    app = models.CharField(verbose_name="应用", max_length=50)
    key = models.CharField(verbose_name="密钥", max_length=200)
