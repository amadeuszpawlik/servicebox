# Generated by Django 2.1.2 on 2018-10-31 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_ticket_customer'),
        ('companies', '0003_auto_20181031_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='tickets',
            field=models.ManyToManyField(blank=True, to='tickets.Ticket'),
        ),
    ]
