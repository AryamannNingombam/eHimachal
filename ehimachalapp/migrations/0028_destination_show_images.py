# Generated by Django 3.0.8 on 2020-07-30 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ehimachalapp', '0027_auto_20200728_0938'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='show_images',
            field=models.BooleanField(default=True),
        ),
    ]