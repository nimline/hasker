# Generated by Django 2.1.7 on 2019-03-13 19:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0010_auto_20190312_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 13, 19, 21, 7, 427844, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 13, 19, 21, 7, 428745, tzinfo=utc)),
        ),
    ]
