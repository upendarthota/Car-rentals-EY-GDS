# Generated by Django 5.0.3 on 2024-03-30 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0022_car_id_alter_car_car_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_id',
            field=models.CharField(default='', max_length=300),
        ),
    ]
