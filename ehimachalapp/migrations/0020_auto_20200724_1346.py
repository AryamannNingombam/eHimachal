# Generated by Django 3.0.8 on 2020-07-24 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ehimachalapp', '0019_accomodation_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accomodation',
            name='accomodation_image',
            field=models.URLField(),
        ),
    ]
