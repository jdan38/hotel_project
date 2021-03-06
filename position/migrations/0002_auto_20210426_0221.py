# Generated by Django 3.1.7 on 2021-04-26 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('position', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='position',
            name='id',
        ),
        migrations.AlterField(
            model_name='position',
            name='job_title',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='position',
            name='photo',
            field=models.ImageField(null=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
