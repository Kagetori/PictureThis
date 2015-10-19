# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20151019_0049'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='salt',
            field=models.CharField(default='', max_length=32),
            preserve_default=False,
        ),
    ]
