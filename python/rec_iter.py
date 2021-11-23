import collections.abc

def rec_iter(_iterable):
    if isinstance(_iterable, collections.abc.Sequence):
        for item in _iterable:
            yield from rec_iter(item)
    else:
        yield _iterable


nested = [
    [1],
    2,
    [
        [3, 4],
        [5],
        6,
        7,
    ],
    [8],
    9,
]

print(*rec_iter(nested))
