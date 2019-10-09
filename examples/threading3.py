'''
We have seen issue with multiple threads accessing a shared resource in threading2.py
This program addresses the issue by using thread synchronization which ensures that only one thread has access to common resource at a given point of time
this is achieved by acquiring the lock, perform the operation and then releasing the lock
Run the program, observe the output to see that the final value is 200K every time
'''
import threading

def increment():
	"""
	function to increment global variable x by 1
	"""
	global x
	x += 1

def increment1Ltimes(lock):
	"""
	call increment function 100000 times.
	But ensure to lock, increment and then release the lock to make sure only one thread has access
	thread lock is obtained outside of this method and passed as an argument
	"""
	for _ in range(100000):
		lock.acquire()
		increment()
		lock.release()

def main_task():
	global x
	# setting global variable x as 0
	x = 0

	# creating a lock
	lock = threading.Lock()

	#creating Thread class instances to call increment1Ltimes method and pass lock
	t1 = threading.Thread(target=increment1Ltimes, args=(lock,))
	t2 = threading.Thread(target=increment1Ltimes, args=(lock,))

	# start threads. Each thread should increment the global value by 1L times. So, the final value should be 2L/200K
	t1.start()
	t2.start()

	# wait until threads finish their job
	t1.join()
	t2.join()

if __name__ == "__main__":
    #Call main_tasks 10 times. Each time the value should increment by 200K times.
    #Print the final value after each iteration to see the global variable value
	for i in range(10):
		main_task()
		print("Iteration {0}: x = {1}".format(i,x))
