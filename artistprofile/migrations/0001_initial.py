# Generated by Django 3.0.2 on 2020-01-06 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artwork', '0004_auto_20200105_2133'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtistProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=12)),
                ('tattoo_artist', models.BooleanField(default=True)),
                ('piercing_artist', models.BooleanField(default=False)),
                ('artwork', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='artwork', to='artwork.Artwork')),
            ],
        ),
    ]
