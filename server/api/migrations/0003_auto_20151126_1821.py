# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='user1_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='game',
            name='user2_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='turn',
            name='guessed_correctly',
            field=models.BooleanField(default=False),
        ),
    ]
