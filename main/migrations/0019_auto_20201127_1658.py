# Generated by Django 3.1.3 on 2020-11-27 11:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20201127_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 27, 16, 58, 46, 429784)),
        ),
    ]
