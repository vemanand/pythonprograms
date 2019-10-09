'''
Sample program showing Synchronization issue when we have multiple threads running and trying to access a shared resource.
Thread synchronization is defined as a mechanism which ensures that two or more concurrent threads do not simultaneously execute the shared resource section
As mentioned in threading1.py, the GIL (Global Interpreter Lock) will allow only one thread to execute but gives an impression that multiple threads are running simultaneously
This results in unpredictable results when the threads try to act on a common resource/code
In this program we will declare a global variable and assign value 0. We create a method to increment this value
We create 2 threads and call this increment function 100k times from both. So, the expected value is 200K once both threads completes the execution
Run the program to see that the result is not 200K all/most of the times. This shows the problem with accessing shared resources when we are multiple threads
threading3.py solves/addresses this problem by performing lock operation
'''

import threading

def increment():
    #Increment global variable value by 1
    global x
    x += 1

def increment1Ltimes():
	"""
	call increment function 100k times.
	this should increase global variable value by 100K
	"""
	for _ in range(100000):
		increment()

#Create two threads and call increment1Ltimes method using both threads
#This should increment the final value by 100K + 100K = 200K times
def main_task():
	global x
	# setting global variable x as 0 everytime
	x = 0

	# creating threads
	t1 = threading.Thread(target=increment1Ltimes)
	t2 = threading.Thread(target=increment1Ltimes)

	# start threads
	t1.start()
	t2.start()

	# wait until threads finish their job
	t1.join()
	t2.join()

if __name__ == "__main__":
    #Call main_task 10 times. After each iteration, print gloabl variable value which should be 200K
    #But you can see that the final value is not 200K most of the times
	for i in range(10):
		main_task()
		print("Iteration {0}: x = {1}".format(i,x))