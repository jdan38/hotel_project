# Generated by Django 3.1.7 on 2021-04-25 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_auto_20210425_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='bed_size',
            field=models.CharField(default='single', max_length=20),
        ),
        migrations.AlterField(
            model_name='listing',
            name='occupancy',
            field=models.IntegerField(max_length=20),
        ),
    ]