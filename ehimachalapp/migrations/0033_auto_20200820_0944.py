# Generated by Django 3.0.8 on 2020-08-20 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ehimachalapp', '0032_auto_20200814_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='content_credit',
            field=models.CharField(default='', max_length=100),
        ),
    ]