# Generated by Django 3.1.7 on 2021-05-01 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='description',
            field=models.CharField(default='pool', max_length=200),
        ),
    ]
