# Generated by Django 2.1.2 on 2018-11-01 20:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tickets', '0005_auto_20181101_2101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='assignees',
        ),
        migrations.AddField(
            model_name='ticket',
            name='assignee',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]