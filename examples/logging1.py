'''
Demo program showing how to log messages to a log file, to have diagnostic information available
Once you run the program you can see that app.log will have the log messages based on the configured log level
Reference: https://www.geeksforgeeks.org/python-add-logging-to-a-python-script/
'''

import logging

def main():
    # Configure the logging system - filename is the log file where you want to write messages, level is the log level
    # Debug level is the lowest and will write all messages. Format argument is optional
    logging.basicConfig(filename='../resources/app.log',
                        level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s')

    # Variables (to make the calls that follow work)
    name = 'Keith Bernard'
    item = '5am club book'
    filename = 'data.csv'
    mode = 'r'

    # Example logging calls (insert into your program)
    #The five logging calls- critical(), error(), warning(), info(), debug() represent different severity levels in decreasing order.
    #The level argument to basicConfig() is a filter. All messages issued at a level lower than this setting will be ignored.
    logging.critical('Person name =  %s ', name)
    logging.error("Couldn't find %r", item)
    logging.warning('Feature is deprecated')
    logging.info('Opening file %r, mode = %r', filename, mode)
    logging.debug('Got here')


if __name__ == '__main__':
    main()

