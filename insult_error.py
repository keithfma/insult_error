import random
from pdb import set_trace


class InsultError(Exception):
    def __new__(cls, *args, **kwargs):
        set_trace()
        insult_cls = random.choice(InsultErrorOption.__subclasses__())
        print('CLASS:', insult_cls)
        if not args:
            args = tuple([random.choice(messages)])
        return insult_cls(*args, **kwargs)


class InsultErrorOption(InsultError):
    def __new__(cls, *args, **kwargs):
        print('CLASS:', cls)
        return Exception.__new__(cls, *args, **kwargs)


class FuckYouBuddy(InsultErrorOption):
    pass


class NotThisAgain(InsultErrorOption):
    pass


class ForGodsSake(InsultErrorOption):
    pass


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

