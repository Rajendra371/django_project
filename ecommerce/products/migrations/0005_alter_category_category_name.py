# Generated by Django 5.0.1 on 2024-01-24 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_products_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='Category_name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
