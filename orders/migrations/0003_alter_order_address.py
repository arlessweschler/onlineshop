# Generated by Django 4.0.5 on 2022-07-19 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_order_first_name_remove_order_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.TextField(verbose_name='адрес'),
        ),
    ]
