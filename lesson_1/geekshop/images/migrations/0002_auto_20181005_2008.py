# Generated by Django 2.1 on 2018-10-05 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='value',
            field=models.ImageField(upload_to='images/%Y/%m/%d/'),
        ),
    ]
