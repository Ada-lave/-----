# Generated by Django 4.1.6 on 2023-03-13 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Earth', '0013_remove_productcard_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcard',
            name='photo',
            field=models.ImageField(default=2, upload_to='Products/photo/'),
            preserve_default=False,
        ),
    ]
