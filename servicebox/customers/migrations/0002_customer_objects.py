# Generated by Django 2.1.3 on 2018-11-08 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0001_initial'),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='objects',
            field=models.ManyToManyField(blank=True, to='objects.Object'),
        ),
    ]