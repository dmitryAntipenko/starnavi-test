# Generated by Django 2.1.3 on 2018-12-03 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socnetapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(auto_created=True, default=0),
        ),
    ]
