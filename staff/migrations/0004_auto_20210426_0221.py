# Generated by Django 3.1.7 on 2021-04-26 02:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_auto_20210426_0136'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='job_description',
            new_name='job_title',
        ),
    ]
