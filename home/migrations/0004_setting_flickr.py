# Generated by Django 3.0.4 on 2020-03-28 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200328_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='flickr',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]