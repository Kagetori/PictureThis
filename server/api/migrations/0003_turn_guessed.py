# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20151028_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='turn',
            name='guessed',
            field=models.BooleanField(default=False),
        ),
    ]
