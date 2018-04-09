# Generated by Django 2.0.4 on 2018-04-05 17:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='amper',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='dt',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 5, 20, 40, 53, 225467)),
        ),
        migrations.AlterField(
            model_name='record',
            name='volt',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='watt',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='watt_hour',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
