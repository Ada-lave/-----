# Generated by Django 4.1.7 on 2023-03-08 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Earth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profileuser',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='vegetablecard',
            name='slug',
        ),
    ]
