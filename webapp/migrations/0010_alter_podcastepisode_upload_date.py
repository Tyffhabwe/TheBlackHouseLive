# Generated by Django 3.2.9 on 2022-06-27 01:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_podcastepisode_upload_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcastepisode',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime.now, null=True),
        ),
    ]