# Generated by Django 3.2.18 on 2023-04-27 23:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('WalletZeply', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='wallet_created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
