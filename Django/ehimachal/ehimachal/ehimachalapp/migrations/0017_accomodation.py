# Generated by Django 3.0.8 on 2020-07-24 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ehimachalapp', '0016_destination_show_demographics'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accomodation',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('address_details', models.TextField()),
                ('pricing_details', models.TextField()),
                ('website_url', models.CharField(blank=True, max_length=100)),
                ('show_website', models.BooleanField(default=True)),
                ('accomodation_destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ehimachalapp.Destination')),
            ],
        ),
    ]
