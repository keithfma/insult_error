import random


errors = [
    'FuckYouBuddy',
    'NotThisAgain',
    'ForGodsSake',
    'AreYouSerious',
    ]

messages = [
    "Your program is bad and you should feel bad",
    "I envy people who have never met you",
    "You're impossible to underestimate",
    "I don't have the time or the crayons to explain this to you",
    "Don't believe everything you think",
    "I hope this isn't your day job",
    "You're killing your mother right now",
    "I hear that fast food place is still hiring",
    "If you were on fire and I had water, I'd drink it.",
    ]


class InsultError(Exception):

    def __init__(self, *args):
        # hack the error name to be a random insult
        self.__class__.__name__ = random.choice(errors)
        # if no message is provided, select a random insult
        if not args:
            args = tuple([random.choice(messages)])
        self.args = args

