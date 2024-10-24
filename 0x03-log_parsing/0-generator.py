#!/usr/bin/python3
"""
This script generates and prints simulated HTTP GET request logs
to the standard output.
Modules:
    random: Provides functions to generate random numbers.
    sys: Provides access to some variables used
        or maintained by the interpreter.
    time: Provides various time-related functions.
    datetime: Supplies classes for manipulating dates and times.
Functionality:
    - The script runs a loop 1000 times.
    - In each iteration, it sleeps for a random amount of time
        between 0 and 1 second.
    - It then generates a simulated log entry with the following format:
    "{IP_ADDRESS} - [{TIMESTAMP}] \"GET /projects/260 HTTP/1.1\"
    {STATUS_CODE} {RESPONSE_SIZE}"
        where:
            - IP_ADDRESS is a randomly generated IPv4 address.
            - TIMESTAMP is the current date and time.
            - STATUS_CODE is a randomly chosen HTTP status
                code from a predefined list.
            - RESPONSE_SIZE is a randomly generated integer representing
                the size of the response in bytes.
    - The generated log entry is written to the standard output.
    - The output is flushed to ensure it is written immediately.
"""

import random
import sys
from time import sleep
import datetime

# Loop 1000 times to generate log entries
for i in range(1000):
    # Pause execution for a random amount of time between 0 and 1 second
    sleep(random.random())

    # Generate a simulated log entry with a random IP address,
    # current timestamp, random status code, and random response size
    sys.stdout.write("{:d}.{:d}.{:d}.{:d}\
        - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255),  # Generate the first octet of the IP address
        random.randint(1, 255),  # Generate the second octet of the IP address
        random.randint(1, 255),  # Generate the third octet of the IP address
        random.randint(1, 255),  # Generate the fourth octet of the IP address
        datetime.datetime.now(),  # Get the current date and time
        # Randomly choose an HTTP status code
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)  # Generate a random response size in bytes
    ))

    # Flush the output to ensure it is written immediately
    sys.stdout.flush()
