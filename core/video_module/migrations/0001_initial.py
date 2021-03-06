# Generated by Django 4.0 on 2021-12-19 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='YoutubeVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=512)),
                ('description', models.CharField(max_length=1024)),
                ('channel_title', models.CharField(max_length=512)),
                ('thumbnail_url', models.CharField(max_length=512)),
                ('published_at', models.DateTimeField()),
            ],
        ),
    ]
