# Generated by Django 3.0.8 on 2020-07-26 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ehimachalapp', '0022_image_is_title_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='show_video',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='DestinationVideo',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('video_link', models.URLField()),
                ('video_destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ehimachalapp.Destination')),
            ],
        ),
    ]