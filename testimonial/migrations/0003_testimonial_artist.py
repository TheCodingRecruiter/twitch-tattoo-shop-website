# Generated by Django 3.0.2 on 2020-01-10 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonial', '0002_remove_testimonial_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='artist',
            field=models.CharField(default='Jason', max_length=255),
        ),
    ]
