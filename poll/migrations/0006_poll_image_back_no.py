# Generated by Django 3.1.7 on 2021-04-03 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0005_auto_20210403_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='image_back_no',
            field=models.IntegerField(default=0),
        ),
    ]