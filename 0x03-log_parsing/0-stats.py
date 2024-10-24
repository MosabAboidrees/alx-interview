#!/usr/bin/python3
# This script reads lines from standard input (stdin) and computes
# metrics based on the input format. The input format is expected to be:
# <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
# The script skips lines that do not match this format.
# After every 10 lines or upon receiving a keyboard interrupt (CTRL + C),
# it prints the number of lines by status code.
# The possible status codes are: 200, 301, 400, 401, 403, 404, 405, and 500.
# If the status code is not an integer, it is not printed.
# The status codes are printed in ascending order.


# Function to print the metrics
def print_msg(codes, file_size):
    print("File size: {}".format(file_size))
    for key, val in sorted(codes.items()):
        if val != 0:
            print("{}: {}".format(key, val))

# Initialize variables
file_size = 0
code = 0
count_lines = 0

# Dictionary to store the count of each status code
codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

try:
    # Read lines from standard input
    for line in sys.stdin:
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]

        # Check if the line has more than 2 elements
        if len(parsed_line) > 2:
            count_lines += 1

            # Process the first 10 lines
            if count_lines <= 10:
                file_size += int(parsed_line[0])
                code = parsed_line[1]

                # Increment the count for the status code
                # if it is in the dictionary
                if (code in codes.keys()):
                    codes[code] += 1

            # Print the metrics after every 10 lines
            if (count_lines == 10):
                print_msg(codes, file_size)
                count_lines = 0

finally:
    # Print the metrics when the script is interrupted
    print_msg(codes, file_size)
