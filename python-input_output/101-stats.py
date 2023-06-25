#!/usr/bin/python3
import sys

status_counts = {}  # Dictionary to store the counts for each status
total_file_size = 0  # Variable to keep track of the total file size

for line_number, line in enumerate(sys.stdin, 1):
    line_split = line.split()
    status = line_split[-2]
    file_size = int(line_split[-1])

    total_file_size += file_size

    # Update the count for the current status
    status_counts[status] = status_counts.get(status, 0) + 1

    # Print statistics every 10 lines
    if line_number % 10 == 0:
        sorted_statuses = sorted(status_counts.keys())
        print("File size:", total_file_size)
        for status_code in sorted_statuses:
            count = status_counts[status_code]
            print("{}: {}".format(status_code, count))
