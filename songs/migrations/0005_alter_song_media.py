# Generated by Django 3.2.15 on 2022-09-01 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0004_auto_20220901_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='media',
            field=models.ImageField(upload_to=''),
        ),
    ]
