# Generated by Django 2.1.4 on 2019-02-11 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apple', '0007_auto_20190212_0316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='player',
            name='last_name',
        ),
    ]
