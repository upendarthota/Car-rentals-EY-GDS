# Generated by Django 5.0.3 on 2024-03-30 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0011_alter_car_car_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]
