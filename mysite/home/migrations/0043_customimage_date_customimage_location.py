# Generated by Django 4.1.8 on 2023-11-14 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0042_customimage_aperture'),
    ]

    operations = [
        migrations.AddField(
            model_name='customimage',
            name='date',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='customimage',
            name='location',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
