# Generated by Django 5.0.6 on 2024-08-12 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='adress',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='adress',
            new_name='address',
        ),
    ]
