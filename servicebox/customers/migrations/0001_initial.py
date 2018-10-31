# Generated by Django 2.1.2 on 2018-10-30 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('adr_street', models.CharField(max_length=120)),
                ('adr_city', models.CharField(max_length=100)),
                ('adr_postal', models.CharField(max_length=5)),
            ],
        ),
    ]
