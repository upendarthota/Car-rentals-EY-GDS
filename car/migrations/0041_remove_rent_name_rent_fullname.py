# Generated by Django 5.0.3 on 2024-03-30 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0040_alter_rent_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rent',
            name='name',
        ),
        migrations.AddField(
            model_name='rent',
            name='fullname',
            field=models.CharField(default='', max_length=100),
        ),
    ]
