# Generated by Django 3.1.2 on 2022-07-09 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20220709_2218'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.RemoveField(
            model_name='article',
            name='category',
        ),
        migrations.DeleteModel(
            name='ArticleCategory',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
