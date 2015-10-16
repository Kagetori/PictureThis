from django.db import models

# Create your models here.

class User(models.Model):
    """
    Defines a User Object
    """
    name = models.CharField(max_length=256, db_index=True)
    create_date = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=512)
    obfuscated_id = models.IntegerField(db_index=True)

class Friend(models.Model):
    """
    Defines relationships between users
    """
    id1 = models.IntegerField()
    id2 = models.IntegerField()
