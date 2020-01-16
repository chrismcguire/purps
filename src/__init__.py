import ConfigParser

class Upper(object):
    def __init__(self, iterable):
        self._iter = iter(iterable)
    def next(self):
        return next(self._iter).upper()
    def __iter__(self):
        return self

itr = Upper('hello')
print next(itr),
for letter in itr:
    print letter,
