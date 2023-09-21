# Generated by Django 3.0 on 2023-08-21 13:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AntiqueStoreApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='antiqueitem',
            name='starting_price',
        ),
        migrations.AddField(
            model_name='antiqueitem',
            name='startingprice',
            field=models.PositiveIntegerField(default=200),
        ),
        migrations.AddField(
            model_name='antiqueitem',
            name='usitem',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='auction',
            name='highest_bid',
            field=models.PositiveIntegerField(blank=True, default=500, null=True),
        ),
        migrations.AlterField(
            model_name='bid',
            name='bid_amount',
            field=models.PositiveIntegerField(default=200),
        ),
    ]