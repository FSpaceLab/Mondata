# Generated by Django 2.0.4 on 2018-04-10 16:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mon', '0002_auto_20180405_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='dt',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 10, 16, 25, 56, 156549, tzinfo=utc)),
        ),
    ]
