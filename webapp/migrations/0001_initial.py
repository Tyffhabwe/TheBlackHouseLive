# Generated by Django 3.2.9 on 2022-06-23 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('top_text', models.TextField()),
                ('iframe_link', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MeetTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_link', models.TextField()),
                ('writeup', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OnAir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iframe_link', models.TextField()),
                ('video_title', models.CharField(max_length=200)),
                ('video_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='WhatWeDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('right_paragraph', models.TextField()),
                ('left_paragraph', models.TextField()),
            ],
        ),
    ]
