# Generated by Django 4.0.5 on 2022-08-09 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0021_alter_product_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.FloatField(blank=True),
        ),
    ]
