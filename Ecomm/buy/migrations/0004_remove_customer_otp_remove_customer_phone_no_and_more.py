# Generated by Django 4.0.6 on 2022-09-04 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0003_customer_otp_customer_verify_phone_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='otp',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='phone_no',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='verify_phone_no',
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.CharField(default='#', max_length=30),
        ),
        migrations.AddField(
            model_name='customer',
            name='password',
            field=models.CharField(default='#', max_length=20),
        ),
    ]
