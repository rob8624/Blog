# Generated by Django 4.1.8 on 2023-09-19 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0037_alter_customimage_caption'),
    ]

    operations = [
        migrations.AddField(
            model_name='customimage',
            name='shutter',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
