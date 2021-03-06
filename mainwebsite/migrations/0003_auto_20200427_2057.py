# Generated by Django 3.0.5 on 2020-04-28 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainwebsite', '0002_submitedcampaign'),
    ]

    operations = [
        migrations.AddField(
            model_name='submitedcampaign',
            name='brand_approved_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='submitedcampaign',
            name='is_brand_approved',
            field=models.BooleanField(default=False, verbose_name='Is Brand Approved'),
        ),
    ]
