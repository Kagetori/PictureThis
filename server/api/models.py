from django.db import models

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
    id1 = models.IntegerField()
    id2 = models.IntegerField()
    relation = models.IntegerField()

    class Meta:
        index_together = ('id1', 'id2')
