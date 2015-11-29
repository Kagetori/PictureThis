# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20151127_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='wordprompt',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
