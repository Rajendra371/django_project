# Generated by Django 5.0.1 on 2024-01-31 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_status',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
