'''
Sample program to demo threads in Python. The GIL (Global Interpreter Lock) will make sure to run only one thread at any given point of time.
It keeps on switching between threads and works so fast that for human eye, it looks like multiple threads are running in parallel which is not the case
GIL mimics parallelism. Run this program multiple times to observe this behavior - Square and Cube calls are jumbled
Thread() is used to create threads, start() to start thread execution and join() to wait until the thread completes its process
current_thread() is used to get current thread name and main_thread() is used to get main thread name
os.pid() is used to get the process ID. You can see that all threads have the same process ID which means, they share the same CPU process
'''
import threading
import os

def print_square(num):
    print("Thread name running square = {}".format(threading.current_thread().name))
    print("ID of the process running square = {}".format(os.getpid()))
    for i in range(10):
        print("Square = {}".format(num * num))

def print_cube(num):
    print("Thread name running cube = {}".format(threading.current_thread().name))
    print("ID of the process running cube = {}".format(os.getpid()))
    for i in range(10):
        print("Cube = {}".format(num * num * num))

if __name__ == "__main__":
    print("Creating and starting with two threads- one thread calling Square and another Cube")

    print("Main thread name = {}".format(threading.main_thread().name))
    print("ID of the process running main = {}".format(os.getpid()))
    #print("ID of process running main program = {}".format())
    #Create threads by passing the function and arguments. The name argument defines the thread name
    sqthread = threading.Thread(target=print_square, args = (5,),name="Square Thread")
    cuthread = threading.Thread(target=print_cube, args=(3,),name="Cube thread")

    #Start the threads
    sqthread.start()
    cuthread.start()

    #Wait until both threads completes execution
    sqthread.join()
    cuthread.join()

    print("DONE - observe that all process IDs are the same")