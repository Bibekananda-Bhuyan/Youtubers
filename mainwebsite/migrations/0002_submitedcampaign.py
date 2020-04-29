# Generated by Django 3.0.5 on 2020-04-27 02:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainwebsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submitedcampaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submit_url', models.CharField(max_length=1000)),
                ('submit_date', models.DateTimeField(auto_now_add=True)),
                ('campaign', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainwebsite.Campaign')),
            ],
        ),
    ]
