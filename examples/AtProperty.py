'''
Sample program demonstrating the use of @property. This allows you to have virtual attributes in your class.
You can also control the behavior of these attributes - make them read only, control range of values, types etc
'''

class Temperature:
    """Example class to demonstrate virtual attributes using properties"""

    def __init__(self, celsius=0):
        self._celsius = celsius  #The only attribute declared in the class

    @property
    def celsius(self):
        """Fetch the temperature in C"""
        return self._celsius

    @celsius.setter  #This method will be called whenever you assign a value to attribute celsius.
    def celsius(self, value):
        """Store the temperature in C"""
        self._celsius = value

    @property  #This is a dummy/virtual attribute. But we can still work on the attribute fahrenheit as it it exists
    def fahrenheit(self):
        """Return temp in F based on store temp in C"""
        print("Get property on fahrenheit called")
        return (self._celsius * 9) / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        print("Set property on fahrenheit called")
        """store temperature in C"""
        self._celsius = (value - 32) / 9 * 5


temp = Temperature()
print(temp.celsius, temp.fahrenheit)  #This calls get on fahrenheit attribute
temp.celsius = 100 #This calls getter on celsius attribute
print(temp.celsius, temp.fahrenheit)
temp.fahrenheit = -40  #This calls setter method on property fahrenheit
print(temp.celsius, temp.fahrenheit)