# Generated by Django 5.0.3 on 2024-03-30 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0014_alter_car_car_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]