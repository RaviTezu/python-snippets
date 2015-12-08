## Fluent Python Notes:

- The doctest module searches for pieces of text that look like interactive Python sessions, and then executes those sessions to verify that they work exactly as shown.
- The special methods(__gititem__) in Python are also known as dunder methods.

- Named tuple example:
```
>>> Card = collections.namedtuple('Card', ['rank', 'suit'])
>>> beer_card = Card('7', 'diamonds')
>>> beer_card
Card(rank='7', suit='diamonds')
```

- How to pick a random element from a list:
```
>>> from random import choice
>>> choice([1,2,3,4,5])
4
```

- 
