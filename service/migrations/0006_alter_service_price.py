# Generated by Django 3.2.4 on 2021-06-06 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_alter_service_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=8),
        ),
    ]
