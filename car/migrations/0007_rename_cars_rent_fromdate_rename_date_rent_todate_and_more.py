# Generated by Django 5.0.3 on 2024-03-29 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0006_remove_car_id_alter_car_car_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rent',
            old_name='cars',
            new_name='fromdate',
        ),
        migrations.RenameField(
            model_name='rent',
            old_name='date',
            new_name='todate',
        ),
        migrations.AddField(
            model_name='rent',
            name='car_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rent',
            name='totalbill',
            field=models.CharField(default='', max_length=50),
        ),
    ]
