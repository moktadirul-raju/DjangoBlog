# Generated by Django 2.1.4 on 2019-01-30 02:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20190130_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 1, 30, 2, 29, 20, 554230)),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 30, 2, 29, 20, 553786)),
        ),
        migrations.AlterField(
            model_name='reply',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 1, 30, 2, 29, 20, 554680)),
        ),
    ]
