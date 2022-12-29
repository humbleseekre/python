import argparse
import logging


def my_sum(num1, num2):
    print("the sum of two nums is {}".format(num1 + num2))


if __name__ == '__main__':
    # Create a parser object
    parser = argparse.ArgumentParser(description="Add two numbers", prog='test.py')

    # Add arguments
    parser.add_argument('-x', type=int)
    parser.add_argument('-y',  type=int)

    # Parse the incoming arguments
    args = parser.parse_args()

    my_sum(args.x, args.y)

    # Let us Create an object
    logger = logging.getLogger()

    # Now we are going to Set the threshold of logger to DEBUG
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.DEBUG)

    # some messages to test
    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')

'''
The output of the above program would look like this:

WARNING:root:This is a warning message
ERROR:root:This is an error message
CRITICAL:root:This is a critical message
The output shows the severity level before each message along with root, which is the name the 
logging module gives to its default logger. (Loggers are discussed in detail in later sections.) 
This format, which shows the level, name, and message separated by a colon (:), is the default output 
format that can be configured to include things like timestamp, line number, and other details.

Notice that the debug() and info() messages didn’t get logged. This is because, by default, 
the logging module logs the messages with a severity level of WARNING or above. You can change 
that by configuring the logging module to log events of all levels if you want. You can also define your 
own severity levels by changing configurations, but it is generally not recommended as it can cause 
confusion with logs of some third-party libraries that you might be using.

Some of the commonly used parameters for basicConfig() are the following:

level: The root logger will be set to the specified severity level.
filename: This specifies the file.
filemode: If filename is given, the file is opened in this mode. The default is a, which means append.
format: This is the format of the log message.
By using the level parameter, you can set what level of log messages you want to record. 
This can be done by passing one of the constants available in the class, and this would enable all 
logging calls at or above that level to be logged. Here’s an example:

import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug('This will get logged')
'''


