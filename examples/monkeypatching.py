'''
Monkey patching refers to dynamic modifications of a class or module or method at run time.
This program uses the custom module mymodule.py to access the function and changes its behavior
'''

import mymodule

def monkey_func(self):
    print("Monkey function")

#Instantiate the class and call method. Normal behavior
obj1 = mymodule.MyClass()
obj1.func()

#Change the behavior of MyClass function, instantiate the class and call method. Monkey patching
#Observe that the call is made to monkey_func
mymodule.MyClass.func = monkey_func
obj2 = mymodule.MyClass()
obj2.func()
