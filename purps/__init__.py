from __future__ import print_function
from future import standard_library
standard_library.install_aliases()
from builtins import next
from builtins import object

class Upper(object):
    def __init__(self, iterable):
        self._iter = iter(iterable)
    def __next__(self):
        return next(self._iter).upper()
    def __iter__(self):
        return self

itr = Upper('hello')
print(next(itr), end=' ')
for letter in itr:
    print(letter, end=' ')
