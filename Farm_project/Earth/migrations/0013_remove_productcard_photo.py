# Generated by Django 4.1.6 on 2023-03-13 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Earth', '0012_productcard_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcard',
            name='photo',
        ),
    ]
