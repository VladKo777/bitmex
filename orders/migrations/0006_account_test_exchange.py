# Generated by Django 3.0.6 on 2020-06-04 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20200604_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='test_exchange',
            field=models.BooleanField(default=True, verbose_name='TEST_EXCHANGE'),
        ),
    ]
