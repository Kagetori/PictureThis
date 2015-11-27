# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20151126_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='login_token',
            field=models.CharField(max_length=136, null=True),
        ),
    ]
