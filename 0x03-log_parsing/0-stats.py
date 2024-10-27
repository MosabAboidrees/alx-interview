#!/usr/bin/python3
# This script reads lines from standard input (stdin) and computes
# metrics based on the input format. The input format is expected to be:
# <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
# <status code> <file size>
# The script skips lines that do not match this format.
# After every 10 lines or upon receiving a keyboard interrupt (CTRL + C),
# it prints the number of lines by status code.
# The possible status codes are: 200, 301, 400, 401, 403, 404, 405, and 500.
# If the status code is not an integer, it is not printed.
# The status codes are printed in ascending order.

import sys


def print_stats(statistics: dict, total_file_size: int) -> None:
    """Prints the statistics of HTTP status codes and total file size."""
    # Print total file size
    print("File size: {:d}".format(total_file_size))
    # Print each status code count if it has a non-zero value
    for code, count in sorted(statistics.items()):
        if count:
            print("{}: {}".format(code, count))


if __name__ == '__main__':
    # Initialize total file size and line count
    total_file_size, line_count = 0, 0

    # Define valid HTTP status codes to track
    valid_status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    # Initialize status code counts to zero
    statistics = {code: 0 for code in valid_status_codes}

    try:
        # Read each line from standard input
        for line in sys.stdin:
            line_count += 1  # Increment line count
            # Split the line into components based on whitespace
            data = line.split()
            try:
                # Extract the status code (second-to-last item in the line)
                status_code = data[-2]
                # If the status code is one we track, increment its count
                if status_code in statistics:
                    statistics[status_code] += 1
            except IndexError:
                # Skip lines that do not have enough data
                pass
            try:
                # Add the file size (last item in the line) to the total
                total_file_size += int(data[-1])
            except (IndexError, ValueError):
                # Skip lines that do not have a valid file size
                pass
            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats(statistics, total_file_size)
        # Print final stats after processing all lines
        print_stats(statistics, total_file_size)
    except KeyboardInterrupt:
        # Print stats when interrupted
        print_stats(statistics, total_file_size)
        raise

