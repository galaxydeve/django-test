# Generated by Django 3.1.7 on 2022-01-17 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_currency_code', models.CharField(max_length=10)),
                ('from_currency_name', models.CharField(max_length=10)),
                ('to_currency_code', models.CharField(max_length=10)),
                ('to_currency_name', models.CharField(max_length=10)),
                ('exchange_rate', models.FloatField()),
                ('last_refreshed', models.DateTimeField()),
                ('time_zone', models.CharField(max_length=10)),
                ('bid_price', models.FloatField()),
                ('ask_price', models.FloatField()),
            ],
        ),
    ]
