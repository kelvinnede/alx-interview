#!/usr/bin/python3
import sys

def print_stats(total_size, status_codes):
    """Print the total size and status code counts"""
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        if status_codes[code]:
            print(f"{code}: {status_codes[code]}")

# Initialize metrics
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    # Process input lines
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        # Extract and validate file size and status code
        try:
            file_size = int(parts[-1])
            status_code = int(parts[-2])
            total_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1
        except (IndexError, ValueError):
            continue  # Skip if the line doesn't have the correct format

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_stats(total_size, status_codes)

except KeyboardInterrupt:
    pass
finally:
    # Print final statistics before exit
    print_stats(total_size, status_codes)
