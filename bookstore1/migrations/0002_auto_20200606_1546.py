# Generated by Django 3.0.3 on 2020-06-06 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='book_information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=30)),
                ('ISBN', models.CharField(max_length=30, unique=True)),
                ('Author', models.CharField(max_length=30)),
                ('Price', models.FloatField(max_length=30)),
                ('publish_time', models.CharField(max_length=30)),
                ('publisher', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='logged_users',
            name='register_info',
            field=models.CharField(default='11111111111', max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='logged_users',
            name='username',
            field=models.CharField(max_length=10),
        ),
    ]