# Generated by Django 5.0.3 on 2024-03-30 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0037_alter_rent_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent',
            name='order_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]