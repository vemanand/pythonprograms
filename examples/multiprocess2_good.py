'''
This program uses Manager class to create shared data to solve the problem we saw in multiprocess2.py
We can see that the values updated by process P1 are available for the main process
'''

import multiprocessing


def square_list(mylist,records):
	"""
	function to square a given list and add it to the global list
	"""
	#global result
	# append squares of mylist to global list result
	for num in mylist:
		records.append(num * num)
	# print global list result
	print("Global list values (in process p1): {}".format(records))

if __name__ == "__main__":
    with multiprocessing.Manager() as manager:
        # create an empty list in server process memory. This can be shared by all processes
        records = manager.list([])
        # declare some list to send to square_list method to append the square values to above empty list
        mylist = [5, 2, 3, 4]
        # create new process instance using Process class by passing the function and arguments
        p1 = multiprocessing.Process(target=square_list, args=(mylist,records))
        # start the process. This will call the function and copy the squares of given list into global list
        p1.start()
        # wait until process is finished
        p1.join()

        # print global result list values
        print("Global list values (in main program): {}".format(records))