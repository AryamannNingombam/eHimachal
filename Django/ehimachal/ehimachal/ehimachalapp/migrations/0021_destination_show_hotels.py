# Generated by Django 3.0.8 on 2020-07-24 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ehimachalapp', '0020_auto_20200724_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='show_hotels',
            field=models.BooleanField(default=True),
        ),
    ]
