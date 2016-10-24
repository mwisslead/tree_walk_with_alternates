from tree_walk_with_alternates import TreeWalker

levels = ['level1', 'level2']
levels_plural = ['firsts', 'seconds']
data = {
    "level1": {
        "option1": {
            "value1": "level1 = option1"
        },
        "option2": {
            "level2": {
                "option2": {
                    "value1": "level1 = option2, level2 = option2"
                }
            },
            "value2": "level1 = option2"
        }
    },
    "level2": {
        "option1": {
            "value1": "level2 = option1"
        }
    },
    "value1": "top level",
    "value2": "top level"
}

tree = TreeWalker(data, levels, levels_plural)

try:
   tree['Wrong'] = 3
except Exception as err:
    import traceback
    traceback.print_exc(err)
    pass

print(tree['value1'])
print(tree['value2'])
print(tree['firsts'])
tree['level1'] = 'option1'
print(tree['seconds'])
print(tree['value1'])
print(tree['value2'])
tree['level1'] = 'option2'
print(tree['seconds'])
print(tree['value1'])
print(tree['value2'])
tree['level2'] = 'option2'
print(tree['value1'])
print(tree['value2'])
print(tree['value3'])
