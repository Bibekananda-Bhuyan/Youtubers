# Generated by Django 3.0.5 on 2020-04-28 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainwebsite', '0005_creatorinivitation_brand_approved_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_titel', models.CharField(max_length=300)),
                ('notification_massage', models.TextField(max_length=6000)),
                ('notification_for', models.CharField(choices=[('Creator', 'Creator'), ('Brands', 'Brands'), ('Others', 'Others')], default='Creator', max_length=100)),
                ('notification_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
