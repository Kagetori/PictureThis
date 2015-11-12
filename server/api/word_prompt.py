from models import WordPrompt

from interface.word_prompt import WordPrompt as RemoteWord

def get_word_prompt(word):
    if word is None:
        raise RemoteException("Word cannot be blank")
    try:
        word_prompt = WordPrompt.objects.get(word=word)
    except WordPrompt.DoesNotExist:
        raise RemoteException("Word not in database")

    word_class = word_prompt.word_class
    word_category = word_prompt.category
    
    return RemoteWord(word=word, word_class=word_class, word_category=word_category)