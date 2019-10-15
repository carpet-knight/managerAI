from random import choice


class Silvertongue:
    """A class for generating messages using word dictionary."""

    def __init__(self, wordpool):
        # init word dictionary
        self.wordpool = wordpool

    def greet(self, values=None):
        # choose greeting message
        return choice(self.wordpool["start"]).format(values)

    def insist(self):
        # choose stimulating message
        return choice(self.wordpool["mid"])

    def farewell(self):
        # choose farewell message
        return choice(self.wordpool["end"])
