# Generated by Django 4.1.7 on 2023-03-09 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('summary', models.TextField()),
                ('body', models.TextField()),
                ('date', models.DateField()),
                ('pic', models.TextField()),
                ('author', models.CharField(max_length=250)),
            ],
        ),
    ]