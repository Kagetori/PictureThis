# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id1', models.IntegerField()),
                ('id2', models.IntegerField()),
                ('relation', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, db_index=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('password', models.CharField(max_length=512)),
                ('obfuscated_id', models.PositiveIntegerField(db_index=True)),
                ('auth_token', models.UUIDField()),
            ],
        ),
        migrations.AlterIndexTogether(
            name='friend',
            index_together=set([('id1', 'id2')]),
        ),
    ]
