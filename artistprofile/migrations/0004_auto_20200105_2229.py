# Generated by Django 3.0.2 on 2020-01-06 03:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artistprofile', '0003_auto_20200105_2226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artistprofile',
            old_name='artist_name',
            new_name='artist',
        ),
    ]
