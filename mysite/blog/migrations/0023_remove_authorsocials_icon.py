# Generated by Django 4.1.8 on 2023-08-18 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_authorsocials_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authorsocials',
            name='icon',
        ),
    ]
