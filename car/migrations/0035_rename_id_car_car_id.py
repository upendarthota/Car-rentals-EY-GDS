# Generated by Django 5.0.3 on 2024-03-30 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0034_rename_car_id_car_id_alter_contact_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='id',
            new_name='car_id',
        ),
    ]