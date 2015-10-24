from django.db import models

import config
# Create your models here.

class User(models.Model):
    """
    Defines a User Object
    """
    name = models.CharField(max_length=256, db_index=True)
    create_date = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=512)
    obfuscated_id = models.PositiveIntegerField(null=True)
    auth_token = models.UUIDField()

    def __str__(self):
        return 'name %s obfuscated_id %d auth_token %s' % (self.name, self.obfuscated_id, str(self.auth_token))

    def authenticate(self, auth_token):
        return str(self.auth_token) == auth_token

    def get_auth_token(self):
        return str(self.auth_token)

class Friend(models.Model):
    """
    Defines relationships between users
    """
    user_id1 = models.IntegerField()
    user_id2 = models.IntegerField()
    relation = models.IntegerField(default=config.FRIEND_STATUS_REMOVED)

    class Meta:
        index_together = ('user_id1', 'user_id2')

class Group(models.Model):
    """
    Defines an object for a game

    game_id = id
    """
    user_id1 = models.IntegerField()
    user_id2 = models.IntegerField()
    active = models.BooleanField()
    max_rounds = models.IntegerField(default=config.MAX_ROUNDS)
    curr_round = models.IntegerField()
    score = models.IntegerField(default=0)
    create_date = models.DateTimeField(auto_now_add=True)
    last_move_date = models.DateTimeField(auto_now=True)
    game_type = models.IntegerField(default=config.GAME_TYPE_NORMAL)
