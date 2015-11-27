from models import Score

from interface.exception import RemoteException
from interface.score import Score as RemoteScore

# Score api

def get_user_score(user_id):
    """
    API Function to get user's score
    """
    score, _ = Score.objects.get_or_create(user_id=user_id)
    return RemoteScore(points=score.points)

def add_to_score(user_id, points):
    """
    Adds the specified number of points to the score of the
    user with the given user_id

    THIS FUNCTION SHOULD NEVER BE EXPOSED IN URLS AND VIEWS.
    WE DO NOT WANT USERS TO BE ABLE TO ADD IN GAME CURRENCY
    VIA AN API CALL
    """
    if points < 0:
        raise RemoteException('Unable to add negative score')

    try:
        score = Score.objects.get(user_id=user_id)

        score.points += points
        score.save()

        return RemoteScore(points=score.points)

    except Score.DoesNotExist:
        raise RemoteException('Unable to find user score')
