#!/usr/bin/python3
"""Log Parsing Script"""

import sys


def print_stats(total_size, status_codes):
    """Print the accumulated metrics"""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()

        # Check if the line has the correct format
        if len(parts) >= 7:
            # Extract file size
            try:
                file_size = int(parts[-1])
                total_size += file_size
            except ValueError:
                continue

            # Extract status code
            try:
                status_code = int(parts[-2])
                if status_code in status_codes:
                    status_codes[status_code] += 1
            except ValueError:
                continue

            line_count += 1

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

except KeyboardInterrupt:
    print_stats(total_size, status_codes)
    raise

# Print final stats at the end of input
print_stats(total_size, status_codes)
