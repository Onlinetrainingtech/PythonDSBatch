import collections
de=collections.deque('India')
print('deque:',de)
print('Length:',len(de))
print('End:',de[0])
print('Right End:',de[-1])
de.remove('a')
print('After Removing:',de)
print(type(de))
