# Generated by Django 3.0.4 on 2020-03-23 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('new', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.News')),
            ],
        ),
    ]