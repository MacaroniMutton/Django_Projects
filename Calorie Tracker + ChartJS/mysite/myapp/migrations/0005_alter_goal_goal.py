# Generated by Django 5.0.1 on 2024-01-22 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_remove_consume_calorie_goal_goal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='goal',
            field=models.PositiveIntegerField(default=0),
        ),
    ]