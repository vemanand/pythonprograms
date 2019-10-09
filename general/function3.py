'''
Program to demo **kwargs - Passing key values as function arguments.
The double asterisk form of **kwargs is used to pass a keyworded, variable-length argument DICTIONARY to a function.
**kwargs differs from *args in that you will need to assign keywords.
'''

#This method returns true or false based on magicnumber value
def bar(a, b, c, **kwargs):
    return kwargs["magicnumber"] == 7

#Call the above method
if bar(1,2,3,magicnumber = 6) == False:
    print("Great.")
if bar(1,2,3,magicnumber = 7) == True:
    print("Awesome!")

#This method can accept varying number of keyword arguments referred as kwargs
#Note the print method display using format method
def print_names(**kwargs):
    for key, value in kwargs.items():
        print("The value of {} is {}".format(key,value))

#Call the above method
print_names(myname = "Anand", yourname = "Anuradha")
print_names(
name_1="Alex",
name_2="Gray",
name_3="Harper",
name_4="Phoenix",
name_5="Remy",
name_6="Val"
)