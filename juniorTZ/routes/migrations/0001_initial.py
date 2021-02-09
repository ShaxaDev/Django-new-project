# Generated by Django 3.1.5 on 2021-02-04 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cities', '0002_auto_20210202_1359'),
        ('trains', '0003_auto_20210203_0940'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Route number')),
                ('travel_times', models.PositiveSmallIntegerField(verbose_name='RCoute time travel')),
                ('from_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route_from_city_set', to='cities.city', verbose_name='Qaysi shaxardan')),
                ('to_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route_to_city_set', to='cities.city', verbose_name='Qaysi shaxarga')),
                ('trains', models.ManyToManyField(to='trains.Train', verbose_name='Train list')),
            ],
            options={
                'verbose_name': 'Route',
                'verbose_name_plural': 'Routes',
            },
        ),
    ]
