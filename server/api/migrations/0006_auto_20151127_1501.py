# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20151127_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='stars',
            field=models.BigIntegerField(default=10),
        ),
    ]
