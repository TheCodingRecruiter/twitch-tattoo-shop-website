# Generated by Django 3.0.2 on 2020-01-06 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0003_artwork_artwork_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='artwork_title',
            field=models.CharField(default='Artist tattoo design', max_length=255),
        ),
    ]
