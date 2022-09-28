# Generated by Django 4.0.6 on 2022-09-06 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0013_phone_device_storage_phone_os_phone_ram'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgurl', models.CharField(default='#', max_length=100000)),
                ('color', models.CharField(default='#', max_length=100)),
                ('name', models.CharField(default='#', max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='phone',
            name='OS',
            field=models.CharField(default='Android', max_length=10),
        ),
    ]