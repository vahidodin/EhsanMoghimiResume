# Generated by Django 3.2.4 on 2021-06-06 21:09

from django.db import migrations, models
import service.models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to=service.models.get_upload_path),
        ),
    ]
