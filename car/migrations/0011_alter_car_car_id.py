# Generated by Django 5.0.3 on 2024-03-30 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0010_alter_car_car_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]