# Generated by Django 3.2.7 on 2021-11-05 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_rename_orders_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='order',
            name='contact',
            field=models.CharField(default='', max_length=15),
        ),
    ]