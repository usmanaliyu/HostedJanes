# Generated by Django 2.2.10 on 2020-06-28 03:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='disccount_percent',
            new_name='discount_percent',
        ),
    ]
