# Generated by Django 2.0.2 on 2020-07-08 10:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200708_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 8, 10, 12, 42, 644526, tzinfo=utc), verbose_name='Fecha de publicación'),
        ),
    ]
