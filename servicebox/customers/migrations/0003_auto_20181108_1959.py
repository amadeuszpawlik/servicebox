# Generated by Django 2.1.3 on 2018-11-08 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_customer_objects'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='objects',
            new_name='service_objects',
        ),
    ]