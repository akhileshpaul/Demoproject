# Generated by Django 5.1.1 on 2024-10-18 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=255)),
                ('p_phone', models.CharField(max_length=10)),
                ('p_email', models.EmailField(max_length=254)),
                ('booking_data', models.DateField()),
                ('booking_on', models.DateField(auto_now=True)),
            ],
        ),
    ]