# Generated by Django 3.2.9 on 2022-06-26 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_alter_meetteam_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='iframe_link',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
