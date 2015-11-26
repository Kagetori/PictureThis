from models import WordPrompt, User

from interface.exception import RemoteException
from interface.word_prompt import WordPrompt as RemoteWord

import bank

def request_hint(user_id, word):
    if word is None:
        raise RemoteException("Word cannot be blank")
    try:
        word_prompt = WordPrompt.objects.get(word=word)
    except WordPrompt.DoesNotExist:
        raise RemoteException("Word not in database")
    try:
        user = User.objects.get(obfuscated_id=user_id)
    except User.DoesNotExist:
        raise RemoteException("User does not exist")

    word_class = word_prompt.word_class
    word_category = word_prompt.category
    
    return RemoteWord(word=word, word_class=word_class, word_category=word_category)