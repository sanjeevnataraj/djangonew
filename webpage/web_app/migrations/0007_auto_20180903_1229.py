# Generated by Django 2.1 on 2018-09-03 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0006_hobby_details'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hobby_details',
            old_name='student',
            new_name='student1',
        ),
    ]