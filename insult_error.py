import sys
import inspect
import random
from collections import namedtuple, defaultdict

rating_levels = {
    None: 0,
    'PG': 0,
    'R': 1
    }

# insulting exception classes ------------------------------------------------


class FuckYouBuddy(Exception):
    rating='R'


class NotThisAgain(Exception):
    rating='PG'


class ForGodsSake(Exception):
    rating='PG'


# insulting error messages ---------------------------------------------


InsultMessage = namedtuple('InsultMessage', ['message', 'rating'])

feel_bad = InsultMessage(
    message='Your program is bad and you should feel bad',
    rating='PG')

never_met_you = InsultMessage(
    message="I envy people who have never met you.",
    rating='PG')

underestimate = InsultMessage(
    message="You’re impossible to underestimate.",
    rating='PG')

crayons = InsultMessage(
    message="I don’t have the time or the crayons to explain this to you.",
    rating='PG')

dont_believe = InsultMessage(
    message="Don't believe everything you think.",
    rating='PG')


# generic insulting exception ------------------------------------------------
# TODO: switch to a max_rating scheme, so I can use PG for R and not the reverse

def is_exception(obj):
    return inspect.isclass(obj) and issubclass(obj, Exception)

def is_message(obj):
    return isinstance(obj, InsultMessage)

# generate dictionary of exception classes for each rating
insults = defaultdict(list)
for insult_info in inspect.getmembers(sys.modules[__name__], is_exception):
    insult = insult_info[1]
    for this in rating_levels.keys():
        if rating_levels[insult.rating] <= rating_levels[this]:
            insults[this].append(insult)

# generate dictionary of exception messages for each rating
messages = defaultdict(list)
for msg_info in inspect.getmembers(sys.modules[__name__], is_message):
    msg = msg_info[1]
    for this in rating_levels.keys():
        if rating_levels[msg.rating] <= rating_levels[this]:
            messages[this].append(msg.message)

class InsultError(Exception):

    def __new__(cls, *args, rating=None, **kwargs):
        if not rating in insults:
            # fail if user selects an invalid rating
            raise ValueError('Invalid rating argument for InsultError exception')
        if not args:
            # no message, pick one
            message = random.choice(messages[rating])
            args = tuple([message])
        # select and return insulting exception 
        insult = random.choice(insults[rating])
        return insult(*args, **kwargs)

