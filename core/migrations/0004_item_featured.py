# Generated by Django 2.2.10 on 2020-06-01 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200530_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='featured',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
