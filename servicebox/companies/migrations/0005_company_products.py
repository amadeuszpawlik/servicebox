# Generated by Django 2.1.2 on 2018-11-01 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('companies', '0004_company_tickets'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='products',
            field=models.ManyToManyField(blank=True, to='products.Product'),
        ),
    ]
