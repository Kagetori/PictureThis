# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20151023_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='active',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 24, 2, 11, 6, 84530, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='curr_round',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='game_type',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='group',
            name='last_move_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 24, 2, 11, 13, 740374, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='max_rounds',
            field=models.IntegerField(default=6),
        ),
        migrations.AddField(
            model_name='group',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
