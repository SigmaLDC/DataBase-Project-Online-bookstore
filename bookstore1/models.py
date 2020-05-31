from django.db import models

# Create your models here.
class logged_users(models.Model):
    username=models.CharField(max_length=10,unique=True)#字符串类型
    #用户名作为主键，不允许重复
    password=models.CharField(max_length=20)

    class Meta:
        db_table=""

class book_information(models.Model):
    bookname=models.CharField(max_length=30,unique=False)
    ISBN=models.CharField(max_length=30,unique=True)
    Author=models.CharField(max_length=30,unique=False)
    Score=models.FloatField(unique=False)