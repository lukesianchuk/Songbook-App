# Generated by Django 3.2.15 on 2022-08-30 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0002_song_chordlink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='image',
            field=models.FilePathField(path='songs/static/img'),
        ),
    ]