# Generated by Django 4.1.2 on 2022-10-27 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("booking", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="event",
            old_name="seats_available",
            new_name="seats",
        ),
    ]
