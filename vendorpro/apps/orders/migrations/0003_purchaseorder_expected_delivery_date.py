# Generated by Django 5.0.4 on 2024-05-05 22:25

import orders.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_purchaseorder_expected_delivery_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorder',
            name='expected_delivery_date',
            field=models.DateTimeField(default=orders.models.get_default_expected_delivery_date),
        ),
    ]