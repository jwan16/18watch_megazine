# Generated by Django 3.0.3 on 2020-02-11 05:44

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogIndex',
            new_name='BlogIndexPage',
        ),
    ]
