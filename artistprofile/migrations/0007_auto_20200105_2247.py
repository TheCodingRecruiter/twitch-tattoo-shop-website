# Generated by Django 3.0.2 on 2020-01-06 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0004_auto_20200105_2133'),
        ('blog', '0001_initial'),
        ('testimonial', '0002_remove_testimonial_artist'),
        ('artistprofile', '0006_auto_20200105_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artistprofile',
            name='artwork',
            field=models.ManyToManyField(blank=True, to='artwork.Artwork'),
        ),
        migrations.AlterField(
            model_name='artistprofile',
            name='blog_posts',
            field=models.ManyToManyField(blank=True, to='blog.Post'),
        ),
        migrations.AlterField(
            model_name='artistprofile',
            name='customer_testimonials',
            field=models.ManyToManyField(blank=True, to='testimonial.Testimonial'),
        ),
    ]
