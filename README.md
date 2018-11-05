# Intentionally Insulting Exceptions for Python

This package provides a set of insulting exceptions you can use to make your
future self laugh, bother your collaborators, or both.

The core feature is the `InsultError` exception class, which behaves just like
a normal exception with a few differences:
1. The raised error is a randomly-selected subclass with a silly, insulting name
2. If no message is provided, the error will use a random insulting message
3. A special keyword argument `rating` provides some control over how offensive
   you want the error and message to be

Please contribute! This package will be much more fun if not limited to the
measily initial set of options. Obviously, racist, sexist, or other bullshit
jokes are not welcome.

## Example Usage

```python
from insult_error import InsultError, InsultErrors

# raise a random insult with a random message (defaults to "PG" rating)
raise InsultError()
# >>> NotThisAgain: Don't believe everything you think.

# raise a random insult with a user-specified message
raise InsultError('This is my message')
# >>> NotThisAgain: This is my message

# raise a random insult with <= PG rating
raise InsultError(rating="PG")
# >>> ForGodsSake: I don’t have the time or the crayons to explain this to you.

# raise a random insult with <= R rating
raise InsultError(rating="R")
# >>> FuckYouBuddy: I envy people who have never met you.

# catch any of the insult_error exception classes
try:
    raise InsultError()
except InsultErrors
    print('Better luck next time!')
# >>> Better luck next time!
```

One annoying bit of trivia: if you want a random insult exception class, you
must raise the error with parenthesis (i.e., `raise InsultError()` and not
`raise InsultError`)
