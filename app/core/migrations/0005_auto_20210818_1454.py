# Generated by Django 2.2 on 2021-08-18 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_recipe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='minutes',
            new_name='time_minutes',
        ),
    ]
