# Intentionally Insulting Exceptions for Python

This package provides a set of insulting exceptions you can use to make your
future self laugh, bother your collaborators, or both.

The core feature is the `InsultError` exception class, which behaves just like
a normal exception with a few differences:
1. The raised error is a randomly-selected subclass with a silly, insulting name
2. If no message is provided, the error will use a random insulting message
3. A special keyword argument `rating` provides some control over how offensive
   you want the error and message to be (1 being tamest and 10 being meanest)

Please contribute! This package will be much more fun if not limited to the
measily initial set of options. Obviously, racist, sexist, or other bullshit
jokes are not welcome.

## Example Usage

```python
from insult_error import InsultError

# raise a random insult with a random message (defaults to rating=5)
raise InsultError
# >>> NotThisAgain: Don't believe everything you think.

# raise a random insult with a user-specified message
raise InsultError('This is my message')
# >>> NotThisAgain: This is my message

# raise a random insult with <= 2 rating
raise InsultError(rating=2)
# >>> ForGodsSake: I don’t have the time or the crayons to explain this to you.

# raise a random insult with <= 6 rating
raise InsultError(rating=6)
# >>> FuckYouBuddy: I envy people who have never met you.

# handle InsultError exceptions (just like normal, non-insulting errors)
try:
    raise InsultError
except InsultError
    print('Better luck next time!')
# >>> Better luck next time!
```
