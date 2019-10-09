'''
docstrings are used to provide documentation to various Python modules, classes, functions
Content written within triple quotes is considered as docstring. You can also use # for single line docstring
You can retrieve docstring of a given method in 2 ways - using <method name>.__doc__ or help(<method name>)
This sample program demonstrates the same
__doc__ will recognize docstrings only with triple quotes written inside the method
help() will recognize docstrings with triple quotes written above the method or inside the method. It can also identify
single line docstrings written using # ABOVE the method definition
'''


def add(n1,n2):
    '''Function that adds two given numbers and returns the sum'''
    return n1+n2

print(add(10,20))
print("Docstring 1st method: ",add.__doc__)
print("Docstring 2nd method:",end="")
help(add)