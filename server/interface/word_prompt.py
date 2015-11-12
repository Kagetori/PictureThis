from remote_object import RemoteObject

class WordPrompt(RemoteObject):
    def __init__(word, word_class, word_category):
        """
        """
        self.word = word
        self.word_class = word_class
        self.word_category = word_category
