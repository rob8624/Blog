# Generated by Django 4.1.8 on 2023-05-12 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_alter_homepage_hero'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpagegalleryimage',
            name='image',
        ),
        migrations.RemoveField(
            model_name='blogpagegalleryimage',
            name='page',
        ),
        migrations.DeleteModel(
            name='BlogPage',
        ),
        migrations.DeleteModel(
            name='BlogPageGalleryImage',
        ),
    ]
