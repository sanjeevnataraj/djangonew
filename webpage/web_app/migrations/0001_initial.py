# Generated by Django 2.1 on 2018-08-31 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PhoneNumber', models.CharField(default='', max_length=250)),
                ('qualification', models.CharField(default='', max_length=250)),
                ('subjects', models.CharField(default='', max_length=250)),
                ('percentage', models.CharField(default='', max_length=250)),
                ('Description', models.CharField(default='', max_length=250)),
            ],
        ),
    ]
