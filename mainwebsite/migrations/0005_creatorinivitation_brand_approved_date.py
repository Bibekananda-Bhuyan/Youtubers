# Generated by Django 3.0.5 on 2020-04-28 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainwebsite', '0004_auto_20200427_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='creatorinivitation',
            name='brand_approved_date',
            field=models.DateTimeField(null=True),
        ),
    ]
