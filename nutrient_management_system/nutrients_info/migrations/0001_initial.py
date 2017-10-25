# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-23 09:25
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lack', models.BooleanField(default=False)),
                ('surplus', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Geographical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('food',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='nutrients_info.Food')),
            ],
        ),
        migrations.CreateModel(
            name='Nutrient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('avg_intake', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('type', models.CharField(
                    choices=[('athelete', 'athelete'), ('normal', 'normal'),
                             ('pregnant-lady', 'pregnant-lady')],
                    default='athelete', max_length=20)),
                ('nutrient',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='nutrients_info.Nutrient')),
            ],
        ),
        migrations.CreateModel(
            name='Seasonal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('food',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='nutrients_info.Food')),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='nutrient',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='nutrients_info.Nutrient'),
        ),
        migrations.AddField(
            model_name='disease',
            name='nutrient',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='nutrients_info.Nutrient'),
        ),
    ]