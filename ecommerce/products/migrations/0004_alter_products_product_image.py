# Generated by Django 5.0.1 on 2024-01-23 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_products_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_image',
            field=models.FileField(null=True, upload_to='static/uploads'),
        ),
    ]
