import random
from collections import namedtuple


class InsultError(Exception):
    def __init__(self, *args, rating=5):
        # hack the error name to be a random insult rated <= rating
        name = random.choice([x.name for x in names if x.rating <= rating])
        self.__class__.__name__ = name
        # if no message is provided, select a random insult
        if not args:
            msg = random.choice([x.msg for x in messages if x.rating <= rating])
            args = (msg,)
        self.args = args


# insulting error names ----------


Name = namedtuple('Name', ('name', 'rating'))

names = [
    Name(name='FuckYouBuddy', rating=5),
    Name(name='NotThisAgain', rating=1),
    Name(name='ForGodsSake', rating=1),
    Name(name='AreYouSerious', rating=1),
    ]


# insulting error messages ----------


Message = namedtuple('Message', ('msg', 'rating'))

messages = [
    Message(msg="Your program is bad and you should feel bad", rating=1),
    Message(msg="I envy people who have never met you", rating=1),
    Message(msg="You're impossible to underestimate", rating=1),
    Message(msg="I don't have the time or the crayons to explain this to you", rating=1),
    Message(msg="Don't believe everything you think", rating=1),
    Message(msg="I hope this isn't your day job", rating=1),
    Message(msg="You're killing your mother right now", rating=1),
    Message(msg="I hear that fast food place is still hiring", rating=1),
    Message(msg="If you were on fire and I had water, I'd drink it.", rating=1),
    ]

