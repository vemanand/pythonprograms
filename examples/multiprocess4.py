'''
Sample program showing how True parallel processing can be achieved in Python using multiprocessing
Pool() method can be used to create multiple processes and distribute the work/load.
Each worker completes its own task and the final result is aggregated
Once you run this program on a multi-core processing system, you can see different process IDs
'''

# Python program to understand
# the concept of pool
import multiprocessing
import os

#Simple method that returns the square of a given number
def square(n):
	print("Worker process id for {0}: {1}".format(n, os.getpid()))
	return (n*n)

if __name__ == "__main__":
	# Declare a sample list with some numbers
	mylist = [1,2,3,4,5,6,7,8]

	# creating a pool object.
    # Optionally we can specify the number of processes we want to create, max number of tasks you want to assign per child/process
	p = multiprocessing.Pool(s)

	# map the pool to target function along with the parameter/argument
    # In this case, the contents of mylist and square method will be distributed among the cores/processes
	result = p.map(square, mylist)

	print(result)
