# Generated by Django 3.2.4 on 2021-06-06 21:08

from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('status', models.IntegerField(choices=[(1, 'pending'), (2, 'confirmed'), (3, 'rejected')], default=1)),
                ('price', models.DecimalField(decimal_places=0, max_digits=8)),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('serviceId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='service.services')),
            ],
        ),
    ]
