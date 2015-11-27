# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_user_login_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='max_rounds',
            field=models.IntegerField(),
        ),
    ]
