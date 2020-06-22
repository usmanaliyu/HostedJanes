# Generated by Django 2.2 on 2020-06-20 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20200620_1958'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=30)),
                ('message', models.TextField(max_length=300)),
                ('time', models.DateField(auto_now_add=True)),
            ],
        ),
    ]