# Generated by Django 2.1.7 on 2019-03-11 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0005_auto_20190311_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='for_question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='qa.Question'),
            preserve_default=False,
        ),
    ]
