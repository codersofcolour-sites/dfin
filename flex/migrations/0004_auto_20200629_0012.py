# Generated by Django 3.0.7 on 2020-06-28 23:12

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('flex', '0003_auto_20200626_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='flexpage',
            name='banner_cta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page'),
        ),
        migrations.AddField(
            model_name='flexpage',
            name='banner_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='flexpage',
            name='banner_subtitle',
            field=wagtail.core.fields.RichTextField(default='Test text'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flexpage',
            name='banner_title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
