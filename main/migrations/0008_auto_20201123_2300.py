# Generated by Django 3.1.3 on 2020-11-23 17:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20201123_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 23, 23, 0, 16, 371097)),
        ),
    ]