# Generated by Django 4.2.13 on 2024-08-09 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_flight_approved_by_crew_delete_seatreservation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flight',
            old_name='arrival_time',
            new_name='return_time',
        ),
    ]
