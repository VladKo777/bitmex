# Generated by Django 3.0.6 on 2020-06-04 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_account_test_exchange'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.CharField(blank=True, default=None, max_length=50, null=True, unique=True, verbose_name='orderID'),
        ),
    ]
