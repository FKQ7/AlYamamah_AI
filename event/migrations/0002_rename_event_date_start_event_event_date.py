# Generated by Django 5.1.4 on 2024-12-11 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='event_date_start',
            new_name='event_date',
        ),
    ]