# Advanced Python Mastery

my solutions to [Advanced Python Mastery](https://github.com/dabeaz-course/python-mastery) (course by @dabeaz)

## some notes

- you need `range(n)` not `for i in n`
- `.split(" ")` returns `\n`
- `float()` can parse `\n`
- use `with` to prevent file from being left open, but if f is just for reading lines, just do `for line in open('file', 'r')` [source](https://stackoverflow.com/a/13597111)
- use `repr` to show `\n` in print statements
- interactive interpreter doesn't show print statements
- `tracemalloc.get_traced_memory()` to trace memory allocations
- use `__slots__` to explicitly state which instance attributes you expect object instances to have, this allows for [faster](https://stackoverflow.com/questions/472000/usage-of-slots) attribute access and space savings
