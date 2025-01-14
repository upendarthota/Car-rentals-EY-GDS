# Generated by Django 5.0.3 on 2024-03-30 18:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0035_rename_id_car_car_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=90)),
                ('email', models.CharField(default='', max_length=50)),
                ('phone', models.CharField(default='', max_length=20)),
                ('address', models.CharField(default='', max_length=500)),
                ('city', models.CharField(default='', max_length=50)),
                ('car_name', models.CharField(default='', max_length=50)),
                ('car_seater', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('car_fuel', models.CharField(default='', max_length=50)),
                ('days_for_rent', models.IntegerField(default=0)),
                ('fromdate', models.DateField(blank=True, default=datetime.datetime.now)),
                ('todate', models.DateField(blank=True, default=datetime.datetime.now)),
                ('loc_from', models.CharField(default='', max_length=50)),
                ('loc_to', models.CharField(default='', max_length=50)),
                ('totalbill', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
