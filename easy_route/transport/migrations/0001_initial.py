# Generated by Django 5.1.6 on 2025-03-01 19:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('gmail', models.EmailField(max_length=250)),
                ('phone', models.CharField(max_length=11)),
                ('photo', models.ImageField(upload_to='drivers')),
            ],
            options={
                'verbose_name': 'Driver',
                'verbose_name_plural': 'Drivers',
            },
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('photo', models.ImageField(upload_to='institutions')),
            ],
            options={
                'verbose_name': 'Institution',
                'verbose_name_plural': 'Institutions',
            },
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('going', models.TimeField()),
                ('back', models.TimeField()),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='routes', to='transport.institution')),
            ],
            options={
                'verbose_name': 'Route',
                'verbose_name_plural': 'Routes',
            },
        ),
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=150)),
                ('plate', models.CharField(max_length=7)),
                ('capacityStudents', models.IntegerField()),
                ('driver', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bus', to='transport.driver')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bus', to='transport.route')),
            ],
            options={
                'verbose_name': 'Bus',
                'verbose_name_plural': 'Bus',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('gmail', models.EmailField(max_length=250)),
                ('phone', models.CharField(max_length=11)),
                ('photo', models.ImageField(upload_to='students')),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='transport.bus')),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
            },
        ),
    ]
