# Generated by Django 4.2.8 on 2024-01-31 13:27

from django.db import migrations
import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0045_alter_blogdetailpage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdetailpage',
            name='content',
            field=wagtail.fields.StreamField([('title_and_text', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Add your title', required=True)), ('text', wagtail.blocks.TextBlock(help_text='Add additional text', required=False))])), ('image', wagtail.blocks.StructBlock([('small_image', wagtail.images.blocks.ImageChooserBlock(blank=True, required=False)), ('medium_image', wagtail.images.blocks.ImageChooserBlock(blank=True, required=False)), ('large_image', wagtail.images.blocks.ImageChooserBlock(blank=True, required=False)), ('text', wagtail.blocks.TextBlock(max_length=200, required=True))])), ('text_body', wagtail.blocks.StructBlock([('rich_text', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'image', 'strikethrough', 'link', 'hr', 'code', 'document-link', 'blockquote'], max_length=2000, required=False))])), ('gallery', wagtail.blocks.StructBlock([('gallery_images', wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock)), ('gallery_heading', wagtail.blocks.TextBlock(max_length=200))])), ('code', wagtail.blocks.StructBlock([('language', wagtail.blocks.ChoiceBlock(choices=[('python', 'python'), ('javascript', 'javascript'), ('css', 'css'), ('html', 'html'), ('django', 'django')])), ('text', wagtail.blocks.TextBlock())])), ('quote', wagtail.blocks.StructBlock([('quote_text', wagtail.blocks.TextBlock(max_length=2000, required=False))])), ('embed', wagtail.blocks.StructBlock([('embed', wagtail.embeds.blocks.EmbedBlock())])), ('full_width_image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(blank=True, required=False)), ('text', wagtail.blocks.TextBlock(max_length=200, required=True))])), ('strava_embed', wagtail.blocks.StructBlock([('code', wagtail.blocks.TextBlock(help_text='Please enter the code \n                               from data-embed-id= section of your Strava Embed code', max_length=50, required=True))])), ('text', wagtail.blocks.CharBlock()), ('slideshow', wagtail.blocks.StructBlock([('slide_images', wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock)), ('slide_heading', wagtail.blocks.TextBlock(max_length=200))])), ('image_group', wagtail.blocks.StructBlock([('group_images', wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock, max_num=2))]))], use_json_field=True),
        ),
    ]
