# Generated by Django 4.1.7 on 2023-03-08 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='fb',
            field=models.CharField(default='-', max_length=250),
        ),
        migrations.AddField(
            model_name='article',
            name='ph',
            field=models.CharField(default='-', max_length=250),
        ),
        migrations.AddField(
            model_name='article',
            name='tw',
            field=models.CharField(default='-', max_length=250),
        ),
        migrations.AddField(
            model_name='article',
            name='yt',
            field=models.CharField(default='-', max_length=250),
        ),
    ]