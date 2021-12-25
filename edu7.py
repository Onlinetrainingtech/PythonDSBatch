import collections
print("Order Dictionary")
d1=collections.OrderedDict()
d1['a']='SAS'
d1['d']='Python'
d1['b']='CProgram'
for k,v in d1.items():
    print(k,":",v)
print("Sorted Order Dictionary")
dict=collections.OrderedDict(sorted(d1.items()))
for k,v in dict.items():
    print(k,":",v)
