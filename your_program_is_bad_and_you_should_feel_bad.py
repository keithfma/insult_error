import sys
import inspect
import random
from collections import namedtuple


# insulting exception classes ------------------------------------------------


class FuckYouBuddy(Exception):
    rating='R'


class NotThisAgain(Exception):
    rating='PG'


# TODO: insulting error messages ---------------------------------------------


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


# generic insulting exception ------------------------------------------------
# TODO: switch to a max_rating scheme, so I can use PG for R and not the reverse

def is_exception(obj):
    return inspect.isclass(obj) and issubclass(obj, Exception)

def is_message(obj):
    return isinstance(obj, InsultMessage)

# generate dictionary of exception classes for each rating
insults = {None: [], 'PG': [], 'R': []}
for insult_info in inspect.getmembers(sys.modules[__name__], is_exception):
    insult = insult_info[1]
    insults[None].append(insult)
    insults[insult.rating].append(insult)

# generate dictionary of exception messages for each rating
messages = {None: [], 'PG': [], 'R': []}
for msg_info in inspect.getmembers(sys.modules[__name__], is_message):
    msg = msg_info[1]
    messages[None].append(msg.message)
    messages[msg.rating].append(msg.message)

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
        insult = random.choice(insults[None])
        return insult(*args, **kwargs)

