# Generated by Django 3.1.7 on 2021-04-26 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='address',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='description',
            field=models.TextField(blank=True, max_length=400),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]
