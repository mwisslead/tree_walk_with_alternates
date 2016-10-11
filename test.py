import json

from tree_walk_with_alternates import TreeWalker

with open('test.json', 'rb') as fid:
    data = json.loads(fid.read().decode('UTF-8'))

tree = TreeWalker(data, ['level1', 'level2'], ['firsts', 'seconds'])

print(tree['value1'])
print(tree['value2'])
tree['level1'] = 'option1'
print(tree['value1'])
print(tree['value2'])
tree['level1'] = 'option2'
print(tree['value1'])
print(tree['value2'])
tree['level2'] = 'option2'
print(tree['value1'])
print(tree['value2'])
