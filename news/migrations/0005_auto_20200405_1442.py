# Generated by Django 3.0.4 on 2020-04-05 11:42

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20200327_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='detail',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
