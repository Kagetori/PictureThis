# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turn',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='api.Game', null=True),
        ),
        migrations.AlterField(
            model_name='turn',
            name='word_prompt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='api.WordPrompt', null=True),
        ),
        migrations.AlterField(
            model_name='wordprompt',
            name='word',
            field=models.CharField(unique=True, max_length=255),
        ),
    ]
