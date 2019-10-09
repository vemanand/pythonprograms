'''
In multiprocess1.py we saw that "multiprocessing" module can be used to create processes
But each process will have its own PID, run in its own memory. In that case we will have an issue when consuming shared resources
This program demonstrates that the changes done by one process for a global List are not available for another process
By running the program you can see that the values updated by Process P1 are NOT available for the main process
Reference: https://www.geeksforgeeks.org/multiprocessing-python-set-2/
'''

import multiprocessing

# Declare empty list with global scope - global list
result = []

def square_list(mylist):
	"""
	function to square a given list and add it to the global list
	"""
	#global result
	# append squares of mylist to global list result
	for num in mylist:
		result.append(num * num)
	# print global list result
	print("Global list values (in process p1): {}".format(result))

if __name__ == "__main__":
	# Declar some input list to pass to the square_list method
	mylist = [5,2,3,4]

	# create new process instance using Process class by passing the function and arguments
	p1 = multiprocessing.Process(target=square_list, args=(mylist,))
	# start the process. This will call the function and copy the squares of given list into global list
	p1.start()
	# wait until process is finished
	p1.join()

	# print global result list values
	print("Global list values (in main program): {}".format(result))