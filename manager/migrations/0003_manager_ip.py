# Generated by Django 4.1.7 on 2023-05-14 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_manager_uname'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='ip',
            field=models.CharField(default='', max_length=250),
        ),
    ]