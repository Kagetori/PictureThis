# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_user_salt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='relation',
            field=models.IntegerField(default=0),
        ),
    ]
