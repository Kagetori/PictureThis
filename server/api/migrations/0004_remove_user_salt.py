# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_user_salt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='salt',
        ),
    ]
