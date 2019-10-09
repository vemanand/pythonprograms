'''
In logging1.py we were able to log messages in to a log file. But the logging configuration is hard coded in the script
This program demos how you can store and manage the configuration in a file
Reference: https://www.geeksforgeeks.org/python-add-logging-to-a-python-script/
'''

import logging
import logging.config

def main():
    # Load the Logging configuraiton from the file
    logging.config.fileConfig('../resources/logconfig.ini')

    # Declare Variables - used below to log the information
    name = 'James Bond'
    item = 'iPhone'
    filename = 'dataset.csv'
    mode = 'r'

    #Log the information using log level methods
    #The five logging calls- critical(), error(), warning(), info(), debug() represent different severity levels in decreasing order.
    #The level argument to basicConfig() is a filter. All messages issued at a level lower than this setting will be ignored.
    logging.critical('Person name =  %s ', name)
    logging.error("Couldn't find %r", item)
    logging.warning('The function is deprecated')
    logging.info('Opening file %r, mode = %r', filename, mode)
    logging.debug('Got here')


if __name__ == '__main__':
    main()