'''
There is no ternary operator in Python. But the below code behaves (mimics) like a ternary operation
'''
a,b = 300, 45
big = a if a>b else b
print("Bigger value = %d" %big)