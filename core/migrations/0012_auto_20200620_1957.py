# Generated by Django 2.2 on 2020-06-20 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20200619_0134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='stripe_charge_id',
            new_name='ref',
        ),
    ]
