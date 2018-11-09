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
    Name(rating=5, name='FuckYouBuddy'),
    Name(rating=1, name='NotThisAgain'),
    Name(rating=1, name='ForGodsSake'),
    Name(rating=1, name='AreYouSerious'),
    ]


# insulting error messages ----------


Message = namedtuple('Message', ('msg', 'rating'))

messages = [
    Message(rating=1, msg="Your program is bad and you should feel bad"),
    Message(rating=1, msg="I envy people who have never met you"),
    Message(rating=1, msg="You're impossible to underestimate"),
    Message(rating=1, msg="I don't have the time or the crayons to explain this to you"),
    Message(rating=1, msg="Don't believe everything you think"),
    Message(rating=1, msg="I hope this isn't your day job"),
    Message(rating=1, msg="You're killing your mother right now"),
    Message(rating=1, msg="I hear that fast food place is still hiring"),
    Message(rating=1, msg="If you were on fire and I had water, I'd drink it."),
    ]

