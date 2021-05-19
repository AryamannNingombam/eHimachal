# Generated by Django 3.0.8 on 2020-07-22 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ehimachalapp', '0011_auto_20200722_1208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destination',
            name='has_short_desc',
        ),
        migrations.RemoveField(
            model_name='destination',
            name='short_desc',
        ),
        migrations.AddField(
            model_name='destination',
            name='is_in_homepage',
            field=models.BooleanField(default=False),
        ),
    ]