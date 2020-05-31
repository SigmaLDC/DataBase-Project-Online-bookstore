from django.db import models

# Create your models here.
class logged_users(models.Model):
    username=models.CharField(max_length=10,unique=True)#字符串类型
    #用户名作为主键，不允许重复
    password=models.CharField(max_length=10)

    class Meta:
        db_table=""