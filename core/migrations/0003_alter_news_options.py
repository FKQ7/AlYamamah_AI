# Generated by Django 5.1.4 on 2024-12-10 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_news_date_end'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-date_start']},
        ),
    ]
