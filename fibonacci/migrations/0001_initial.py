# Generated by Django 2.2 on 2019-04-14 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BinRecord',
            fields=[
                ('bin_number', models.IntegerField(primary_key='True', serialize=False)),
                ('saved_number', models.IntegerField()),
                ('last_number', models.TextField()),
                ('second_last_number', models.TextField()),
            ],
        ),
    ]