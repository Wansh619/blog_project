# Generated by Django 4.0.6 on 2022-09-04 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0006_alter_otp_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
