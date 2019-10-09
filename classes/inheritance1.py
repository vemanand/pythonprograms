'''
Sample program showing simple inheritance
Multiple types of inheritance are possible - Single inheritance, Multi-Level inheritance, Hierarchical inheritance, Multiple inheritance
'''

class base(object):
    var1 = "var1 from base class"
    var2 = "var2 from base class"

#Define a dervied class that inherits base class so it gets all features of the base class
class derived(base):
    pass

print(derived.var1)
print(derived.var2)