# Generated by Django 2.1.7 on 2019-03-12 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0007_auto_20190311_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
