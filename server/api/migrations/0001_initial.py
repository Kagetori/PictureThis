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
                ('user_id1', models.IntegerField()),
                ('user_id2', models.IntegerField()),
                ('relation', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id1', models.IntegerField()),
                ('user_id2', models.IntegerField()),
                ('active', models.BooleanField()),
                ('max_rounds', models.IntegerField(default=6)),
                ('curr_round', models.IntegerField()),
                ('score', models.IntegerField(default=0)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('last_move_date', models.DateTimeField(auto_now=True)),
                ('game_type', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Turn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('turn_num', models.IntegerField()),
                ('game', models.ForeignKey(to='api.Game')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, db_index=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('password', models.CharField(max_length=512)),
                ('obfuscated_id', models.PositiveIntegerField(null=True)),
                ('auth_token', models.UUIDField()),
            ],
        ),
        migrations.CreateModel(
            name='WordPrompt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word', models.CharField(max_length=512)),
            ],
        ),
        migrations.AddField(
            model_name='turn',
            name='word_prompt',
            field=models.ForeignKey(to='api.WordPrompt'),
        ),
        migrations.AddField(
            model_name='game',
            name='words_seen',
            field=models.ManyToManyField(to='api.WordPrompt', through='api.Turn'),
        ),
        migrations.AlterIndexTogether(
            name='friend',
            index_together=set([('user_id1', 'user_id2')]),
        ),
    ]
