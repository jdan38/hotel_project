# Generated by Django 3.1.7 on 2021-04-09 06:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hotels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('staff_id', models.AutoField(primary_key=True, serialize=False)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('jobtitle', models.CharField(max_length=200)),
                ('level', models.CharField(max_length=200)),
                ('job_description', models.TextField(blank=True)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('is_eom', models.BooleanField(default=False)),
                ('hire_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('payrate', models.IntegerField()),
                ('paytype', models.CharField(max_length=20)),
                ('hotel_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hotels.hotel')),
            ],
        ),
    ]
