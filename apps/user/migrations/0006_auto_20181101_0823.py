# Generated by Django 2.1.1 on 2018-11-01 08:23

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Update the item input date of an item in the bag.
    """
    dependencies = [
        ('user', '0005_auto_20181024_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bagitemmodel',
            name='inputted_time',
            field=models.DateField(default=datetime.datetime.now, help_text='item entry bag date'),
        ),
    ]
