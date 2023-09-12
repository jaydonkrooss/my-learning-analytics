# Generated by Django 3.2.20 on 2023-09-06 18:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0025_remove_courseviewoption_show_assignment_planning_v1'),
    ]

    # Initially set this to null but alter it to default to the current date
    operations = [
        migrations.AddField(
            model_name='course',
            name='date_created',
            field=models.DateTimeField(default=None, null=True, blank=True, verbose_name='Date course was created'),
        ),
        migrations.AlterField(
            model_name='course',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='Date course was created'),
        ),
    ]
