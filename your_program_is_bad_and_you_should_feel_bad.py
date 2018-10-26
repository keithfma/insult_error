
class FuckYouBuddy(Exception):
    rating='R'

class NotThisAgain(Exception):
    rating='PG'

class InsultError(Exception):

    def __new__(cls, *args, rating=None, **kwargs):
        if rating is None:
            return NotThisAgain(*args, **kwargs)
        elif rating == 'PG':
            return NotThisAgain(*args, **kwargs)
        elif rating == 'R':     
            return FuckYouBuddy(*args, **kwargs)
        else:
            raise ValueError('Invalid rating for InsultError exception')

