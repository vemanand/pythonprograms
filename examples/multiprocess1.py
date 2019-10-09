'''
Sample program to demo multiprocessing in Python. Each process will have its own PID and run independently
we create 2 processes and call square(), cube() from each
Reference: 
'''

import multiprocessing
import os

#Function that prints the square of the given number 10 times. Observe the use of underscore variable in for loop
def print_square(num):
    print("ID of the process running square = {}".format(os.getpid()))
    for _ in range(10):
        print("Square = {}".format(num * num))

#Function that prints the cube of the given number 10 times. Observe the use of underscore variable in for loop
def print_cube(num):
    print("ID of the process running cube = {}".format(os.getpid()))
    for _ in range(10):
        print("Cube = {}".format(num * num * num))

if __name__ == "__main__":
    print("Creating and starting with two processes - one process calling Square and another Cube")

    print("ID of the process running main = {}".format(os.getpid()))
    #print("ID of process running main program = {}".format())
    #Create threads by passing the function and arguments. The name argument defines the thread name
    p1 = multiprocessing.Process(target=print_square, args = (5,))
    p2 = multiprocessing.Process(target=print_cube, args=(3,))

    #Start the processes
    p1.start()
    p2.start()

    print("ID of the process p1 = {}".format(p1.pid))
    print("ID of the process p2 = {}".format(p2.pid))

    #Wait until both processess completes execution
    p1.join()
    p2.join()

    print("DONE - observe that each Process ID is different")

    # check if any process is still alive - this should not be the case
    print("Process p1 is alive: {}".format(p1.is_alive()))
    print("Process p2 is alive: {}".format(p2.is_alive()))