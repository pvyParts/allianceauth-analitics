# Generated by Django 2.2 on 2019-11-11 13:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authanalitics', '0006_auto_20191109_0716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aacharacter',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 1, 13, 2, 13, 117250)),
        ),
        migrations.AlterField(
            model_name='aazkillmonth',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 1, 13, 2, 13, 118318)),
        ),
    ]