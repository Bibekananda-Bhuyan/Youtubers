# Generated by Django 3.0.5 on 2020-04-29 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainwebsite', '0006_notification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brands_invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Invitations_send_date', models.DateTimeField(auto_now_add=True)),
                ('Campaign', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainwebsite.Campaign')),
                ('Creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainwebsite.Creator')),
            ],
        ),
    ]