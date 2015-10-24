# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20151020_1303'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id1', models.IntegerField()),
                ('user_id2', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='friend',
            old_name='id1',
            new_name='user_id1',
        ),
        migrations.RenameField(
            model_name='friend',
            old_name='id2',
            new_name='user_id2',
        ),
        migrations.AlterIndexTogether(
            name='friend',
            index_together=set([('user_id1', 'user_id2')]),
        ),
    ]
