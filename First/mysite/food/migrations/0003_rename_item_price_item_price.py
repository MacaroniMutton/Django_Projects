# Generated by Django 4.2 on 2024-01-09 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_rename_price_item_item_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='item_price',
            new_name='price',
        ),
    ]