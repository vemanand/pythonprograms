'''
As shown in multiprocess2.py the global variable (List) values updated by the process p1 are not available for main process
To overcome this issue, you need a way to share data between/among processes.
The multiprocessing module provides Array and Value objects to share data between processes. This uses shared memory
Other efficient way to sharing data with processes is to use server process that can hold python objects and allow other
processes to manipulate or access them using proxies. Manager class controls the server process. Hence it provides a way to
create data that can be shared between different processes. This is more flexible than shared memory.
This program demos the use of Manager class to share data between processes
Here we write print_record and insert_record methods. We use one process to insert data and another to print data
Reference: https://www.geeksforgeeks.org/multiprocessing-python-set-2/
multiprocessing has Queue() and Pipe() available for effective communication of different processes.
Use above reference URL to study more, if you are interested. Just know that Queue() takes care of synchronization as well
Synchronization and polling: https://www.geeksforgeeks.org/synchronization-pooling-processes-python/
'''

import multiprocessing

def print_records(records):
    '''
    Funtion to display all records of the list
    :param records: List containing tuple records
    :return: None. Just displays each tuple values in the list
    '''
    for tup in records:
        print("Name = {0} Score = {1}\n".format(tup[0], tup[1]))

def insert_record(record, records):
	"""
	function to add a new record(tuple) to records(list)
	"""
	records.append(record)
	print("New record/tuple {} added!\n".format(record))

if __name__ == '__main__':
	with multiprocessing.Manager() as manager:
		# create a list in server process memory. This can be shared by all processes
		records = manager.list([('Sam', 10), ('Adam', 9), ('Kevin',9)])
		# new record to be inserted in records
		new_record = ('Jeff', 8)

		# create 2 new processes - one to append the new record and another to display all records
		p1 = multiprocessing.Process(target=insert_record, args=(new_record, records))
		p2 = multiprocessing.Process(target=print_records, args=(records,))

		# Run process p1 to insert/append new record
		p1.start()
		p1.join()

		# Run process p2 to print records
		p2.start()
		p2.join()


