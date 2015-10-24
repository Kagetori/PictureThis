# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20151023_1911'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id1', models.IntegerField()),
                ('user_id2', models.IntegerField()),
                ('active', models.BooleanField()),
                ('max_rounds', models.IntegerField(default=6)),
                ('curr_round', models.IntegerField()),
                ('score', models.IntegerField(default=0)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('last_move_date', models.DateTimeField(auto_now=True)),
                ('game_type', models.IntegerField(default=1)),
            ],
        ),
        migrations.DeleteModel(
            name='Group',
        ),
    ]
