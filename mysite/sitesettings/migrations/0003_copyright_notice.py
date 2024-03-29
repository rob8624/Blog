# Generated by Django 4.1.8 on 2023-10-10 12:02

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0083_workflowcontenttype'),
        ('sitesettings', '0002_privacy_notice_notice'),
    ]

    operations = [
        migrations.CreateModel(
            name='copyright_notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('copyright_info', wagtail.fields.RichTextField(default='privacy')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
