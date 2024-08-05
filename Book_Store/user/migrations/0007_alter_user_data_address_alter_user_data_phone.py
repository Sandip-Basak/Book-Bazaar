# Generated by Django 5.0.7 on 2024-08-05 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_user_data_address_alter_user_data_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_data',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='phone',
            field=models.DecimalField(decimal_places=0, max_digits=10, null=True),
        ),
    ]