from remote_object import RemoteObject

class WordPrompt(RemoteObject):
    def __init__(self, word, word_class, word_category, bank_account):
        """
        word
            the word
        word_class
            part of speech, e.g. noun
        word_category
            another grouping of a word, e.g. food
        bank_account
            bank account of user
        """
        self.word = word
        self.word_class = word_class
        self.word_category = word_category
        self.bank_account = bank_account
