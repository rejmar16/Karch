# Generated by Django 4.2.5 on 2023-09-27 07:16

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_alter_project_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='text',
            field=tinymce.models.HTMLField(default='NA', max_length=1000),
        ),
    ]