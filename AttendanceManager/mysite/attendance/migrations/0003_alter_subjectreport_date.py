# Generated by Django 4.2 on 2024-01-17 12:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_alter_subject_classes_attended_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectreport',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]