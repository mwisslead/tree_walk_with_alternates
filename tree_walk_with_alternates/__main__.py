import sys
import json

from tree_walk_with_alternates import TreeWalker

def main(argv=None):
    if not argv or len(argv) < 2: 
        return
    with open(argv[1], 'rb') as fid:
        data = fid.read()
        jsondata = json.loads(data)
    levels = jsondata.pop('Data Levels')
    return TreeWalker(jsondata, [i[0] for i in levels], [i[1] for i in levels])

if __name__ == '__main__':
    print(main(sys.argv))
    sys.exit()
