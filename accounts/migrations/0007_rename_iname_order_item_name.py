# Generated by Django 5.0.6 on 2024-06-05 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_order_iname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='iname',
            new_name='item_name',
        ),
    ]
