# Generated by Django 2.2 on 2020-06-18 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_homepagebanner_homesidebanner_shopbottombanner_shoptopbanner_slider'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepagebanner',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homesidebanner',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='shopbottombanner',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='shoptopbanner',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]