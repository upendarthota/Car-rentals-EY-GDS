# Generated by Django 5.0.3 on 2024-03-30 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0017_rent_id_alter_rent_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='car',
            name='car_id',
            field=models.IntegerField(default=0),
        ),
    ]
