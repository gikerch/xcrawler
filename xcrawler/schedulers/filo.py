"""
    filo scheduler
    ~~~~~~~~~~~~~~
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

from collections import deque


class FILOScheduler(object):
    def __init__(self):
        self._requests = deque()

    def __repr__(self):
        return 'FILOScheduler()'

    def add(self, req):
        self._requests.append(req)

    def pop(self):
        try:
            return self._requests.pop()
        except IndexError:
            return None

    def clear(self):
        self._requests.clear()

    def __len__(self):
        return len(self._requests)
