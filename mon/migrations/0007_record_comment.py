# Generated by Django 2.0.4 on 2018-04-10 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mon', '0006_auto_20180410_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='comment',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]