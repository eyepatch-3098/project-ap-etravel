# Generated by Django 3.1.3 on 2020-11-23 17:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20201122_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='hotel_city',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 23, 22, 42, 27, 811348)),
        ),
    ]
