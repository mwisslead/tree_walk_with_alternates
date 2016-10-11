from __future__ import print_function

import sys
import json

def _valid_descents(items):
    if len(items) < 1:
        return []
    if len(items) == 1:
        return [items]
    retval = []
    for i in range(1,len(items)):
        for x in _valid_descents(items[i:]):
            retval.append([items[0]] + x)
    return retval

class TreeWalker(object):
    def __init__(self, input_dict, levels, levels_plural):
        self._data = input_dict
        self._levels = levels
        self._levels_plural = levels_plural
        self._settings = {}

    def _find_item(self, key, max_level=-1):
        levels = self._levels
        if max_level>=0:
            levels = self._levels[:max_level]
        for pattern in _valid_descents([None] + levels + [None]):
            data = self._data
            try:
                for level in pattern[1:-1]:
                    data = data[level]
                    data = data[self[level]]
                return data[key]
            except KeyError:
                pass
        return self._data[key]

    def __getitem__(self, key):
        if key in self._levels:
            return self._settings[key]
        if key  in self._levels_plural:
            ind = self._levels_plural.index(key)
            return list(self._find_item(self._levels[ind], ind).keys())
        return self._find_item(key)

    def __setitem__(self, key, val):
        self._settings[key] = val

    def keys(self):
        return self._levels + self._levels_plural
