# Generated by Django 5.0.6 on 2024-06-05 06:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_order_remove_item_status_item_description_item_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cname',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.customer'),
        ),
    ]