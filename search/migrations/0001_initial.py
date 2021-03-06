# Generated by Django 2.0.13 on 2019-09-01 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=50)),
                ('road_address_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('in_seoul', models.BooleanField()),
                ('x', models.CharField(max_length=20)),
                ('y', models.CharField(max_length=20)),
                ('stock', models.IntegerField(default=0)),
            ],
        ),
    ]
