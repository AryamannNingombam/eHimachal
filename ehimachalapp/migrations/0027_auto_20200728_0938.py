# Generated by Django 3.0.8 on 2020-07-28 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ehimachalapp', '0026_image_image_online_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_online_url',
            field=models.CharField(default='', max_length=1000000),
        ),
    ]
