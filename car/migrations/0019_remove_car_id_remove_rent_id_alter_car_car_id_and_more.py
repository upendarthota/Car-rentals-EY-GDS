# Generated by Django 5.0.3 on 2024-03-30 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0018_car_id_alter_car_car_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='id',
        ),
        migrations.RemoveField(
            model_name='rent',
            name='id',
        ),
        migrations.AlterField(
            model_name='car',
            name='car_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='rent',
            name='order_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]
