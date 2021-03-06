# Generated by Django 2.1.4 on 2019-02-17 11:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20190213_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 17, 11, 46, 2, 224865)),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(related_name='categories', to='blog.Category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 17, 11, 46, 2, 223574)),
        ),
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(related_name='tags', to='blog.Tag'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 2, 17, 11, 46, 2, 225326)),
        ),
    ]
