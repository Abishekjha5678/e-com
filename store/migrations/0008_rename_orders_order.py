# Generated by Django 3.2.7 on 2021-11-05 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_orders'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Orders',
            new_name='Order',
        ),
    ]
