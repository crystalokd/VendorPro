# Generated by Django 5.0.4 on 2024-05-05 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchaseorder',
            name='expected_delivery_date',
        ),
    ]
