# Generated by Django 2.1 on 2018-09-03 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0007_auto_20180903_1229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hobby_details',
            old_name='student1',
            new_name='student',
        ),
        migrations.AlterField(
            model_name='hobby_details',
            name='hobby',
            field=models.CharField(max_length=256),
        ),
    ]
