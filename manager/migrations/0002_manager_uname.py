# Generated by Django 4.1.7 on 2023-03-21 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='uname',
            field=models.CharField(default='', max_length=250),
        ),
    ]