# Generated by Django 3.0.8 on 2020-07-18 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ehimachalapp', '0005_remove_image_file_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image_source',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
