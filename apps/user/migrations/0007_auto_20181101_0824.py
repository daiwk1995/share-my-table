# Generated by Django 2.1.1 on 2018-11-01 08:24

from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Update item expiration date
    """
    dependencies = [
        ('user', '0006_auto_20181101_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bagitemmodel',
            name='expire_time',
            field=models.DateField(blank=True, help_text='item expiration date', null=True),
        ),
    ]
