# Generated by Django 3.0.8 on 2020-07-31 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ehimachalapp', '0028_destination_show_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForError',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='ErrorComplaints/')),
            ],
        ),
    ]
