# Generated by Django 4.1.8 on 2023-05-01 00:11

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_alter_homepage_hero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='hero',
            field=wagtail.fields.StreamField([('hero', wagtail.blocks.StructBlock([('Title', wagtail.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())]))], use_json_field=True),
        ),
    ]
