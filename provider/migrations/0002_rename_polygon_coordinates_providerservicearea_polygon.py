# Generated by Django 3.2.5 on 2021-08-01 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='providerservicearea',
            old_name='polygon_coordinates',
            new_name='polygon',
        ),
    ]
