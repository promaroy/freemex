# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-01 23:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_stock_last_updated'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('isBought', models.BooleanField(default=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=19)),
                ('logtime', models.DateTimeField()),
                ('change', models.DecimalField(decimal_places=2, default=0, max_digits=19)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Player')),
            ],
        ),
        migrations.AddField(
            model_name='playerstock',
            name='invested',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=19),
        ),
        migrations.AlterField(
            model_name='stock',
            name='last_updated',
            field=models.DateTimeField(),
        ),
        migrations.AddField(
            model_name='log',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Stock'),
        ),
    ]