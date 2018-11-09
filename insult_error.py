import random


# define classes -------------------------------------------------------------


class ErrorName:
    def __init__(self, name: str, rating: int):
        assert name, 'name must not be empty'
        assert rating >= 1 and rating <=10, 'rating must be in the range 1-10'
        self.name = name
        self.rating = rating
       
 
class ErrorMessage:
    def __init__(self, msg: str, rating: int):
        assert msg, 'msg must not be empty'
        assert rating >= 1 and rating <=10, 'rating must be in the range 1-10'
        self.msg = msg
        self.rating = rating


class InsultError(Exception):
    def __init__(self, *args, rating=5):
        # hack the error name to be a random insult rated <= rating
        names = [e.name for e in error_name_options if e.rating <= rating]
        self.__class__.__name__ = random.choice(names)
        # if no message is provided, select a random insult
        if not args:
            msgs = [m.msg for m in error_message_options if m.rating <= rating] 
            args = tuple([random.choice(msgs)])
        self.args = args


# define insults to choose from ----------------------------------------------


error_name_options = [
    ErrorName(name='FuckYouBuddy', rating=5),
    ErrorName(name='NotThisAgain', rating=1),
    ErrorName(name='ForGodsSake', rating=1),
    ErrorName(name='AreYouSerious', rating=1),
    ]

error_message_options = [
    ErrorMessage(msg="Your program is bad and you should feel bad", rating=1),
    ErrorMessage(msg="I envy people who have never met you", rating=1),
    ErrorMessage(msg="You're impossible to underestimate", rating=1),
    ErrorMessage(msg="I don't have the time or the crayons to explain this to you", rating=1),
    ErrorMessage(msg="Don't believe everything you think", rating=1),
    ErrorMessage(msg="I hope this isn't your day job", rating=1),
    ErrorMessage(msg="You're killing your mother right now", rating=1),
    ErrorMessage(msg="I hear that fast food place is still hiring", rating=1),
    ErrorMessage(msg="If you were on fire and I had water, I'd drink it.", rating=1),
    ]

