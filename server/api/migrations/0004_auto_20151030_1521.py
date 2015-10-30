# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_turn_guessed'),
    ]

    operations = [
        migrations.AddField(
            model_name='turn',
            name='picture_seen',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='turn',
            name='picture_seen_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='turn',
            name='picture_url',
            field=models.CharField(default='', max_length=512),
            preserve_default=False,
        ),
        migrations.AlterIndexTogether(
            name='game',
            index_together=set([('user_id1', 'user_id2', 'active')]),
        ),
    ]
