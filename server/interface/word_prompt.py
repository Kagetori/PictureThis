from remote_object import RemoteObject

class WordPrompt(RemoteObject):
    def __init__(word, word_class, word_category):
        """
        word
            the word
        word_class
            part of speech, e.g. noun
        word_category
            another grouping of a word, e.g. food
        """
        self.word = word
        self.word_class = word_class
        self.word_category = word_category
