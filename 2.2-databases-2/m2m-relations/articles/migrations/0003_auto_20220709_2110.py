# Generated by Django 3.1.2 on 2022-07-09 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20220709_1855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='article',
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(related_name='articles', through='articles.ArticleCategory', to='articles.Category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=40, verbose_name='Название'),
        ),
    ]
