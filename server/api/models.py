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
    login_token = models.CharField(max_length=136, null=True)

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
        unique_together = ('user_id1', 'user_id2')

class WordPrompt(models.Model):
    """
    A word prompt given to the user
    """
    word = models.CharField(max_length=31, unique=True)
    word_class = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    active = models.BooleanField(default=True)

class Game(models.Model):
    """
    Defines an object for a game
    """
    user_id1 = models.IntegerField()
    user_id2 = models.IntegerField()
    active = models.BooleanField()
    max_rounds = models.IntegerField()
    curr_round = models.IntegerField()
    score = models.IntegerField(default=0)
    create_date = models.DateTimeField(auto_now_add=True)
    last_move_date = models.DateTimeField(auto_now=True)
    game_type = models.IntegerField(default=config.GAME_TYPE_NORMAL)
    user1_score = models.IntegerField(default=0)
    user2_score = models.IntegerField(default=0)

    class Meta:
        index_together = ('user_id1', 'user_id2', 'active')

class Turn(models.Model):
    """
    Defines a turn in the game
    """
    turn_num = models.IntegerField()
    game_id = models.IntegerField()
    word_prompt_id = models.IntegerField();
    guessed = models.BooleanField(default=False)
    guessed_correctly = models.BooleanField(default=False)
    picture_added = models.BooleanField(default=False)
    picture_seen = models.BooleanField(default=False)
    picture_seen_date = models.DateTimeField(null=True)

    class Meta:
        unique_together = ('game_id', 'turn_num')

class Bank(models.Model):
    """
    Defines in-game currency for users
    """
    user_id = models.IntegerField(unique=True, db_index=True)
    stars = models.BigIntegerField(default=config.DEFAULT_STARS)

class Score(models.Model):
    """
    Defines in-game score for users
    """
    user_id = models.IntegerField(unique=True, db_index=True)
    points = models.BigIntegerField(default=0)
