# Generated by Django 4.2.8 on 2024-01-21 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0044_formpage_alter_customrendition_file_formfield'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='search_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='home.customimage', verbose_name='Search image'),
        ),
    ]