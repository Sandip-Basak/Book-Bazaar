# Generated by Django 5.0.7 on 2024-08-04 15:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_inventory'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Order Date')),
                ('quantity', models.DecimalField(decimal_places=0, max_digits=10)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_order', to='store.book', verbose_name='Book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_order', to=settings.AUTH_USER_MODEL, verbose_name='Name')),
            ],
        ),
    ]
