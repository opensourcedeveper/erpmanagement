# Generated by Django 4.2.11 on 2024-03-07 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('vendor_id', models.AutoField(primary_key=True, serialize=False)),
                ('vendor_name', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
    ]
