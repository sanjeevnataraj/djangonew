# Generated by Django 2.1 on 2018-09-07 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0013_auto_20180907_0611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hobby_details',
            name='hobby',
            field=models.CharField(max_length=256),
        ),
    ]