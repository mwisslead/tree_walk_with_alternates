def _find_key(data, key, levels):
    for i, (level, setting) in enumerate(levels):
        try:
            return _find_key(data[level][setting], key, levels[i+1:])
        except:
            pass
    return data[key]

class TreeWalker(object):
    def __init__(self, input_dict, levels, levels_plural):
        self._data = input_dict
        self._levels = levels
        self._levels_plural = levels_plural
        self._settings = {}
        for level in levels:
            self._settings[level] = None

    def __getitem__(self, key):
        if key in self._levels:
            return self._settings[key]
        if key  in self._levels_plural:
            ind = self._levels_plural.index(key)
            key = self._levels[ind]
            levels = [(level, self._settings[level]) for level in self._levels[:ind]]
            return list(_find_key(self._data, key, levels))
        return _find_key(self._data, key, [(level, self._settings[level]) for level in self._levels])

    def __setitem__(self, key, val):
        if key not in self._levels:
            raise KeyError(key)
        self._settings[key] = val

    def keys(self):
        return self._levels + self._levels_plural
