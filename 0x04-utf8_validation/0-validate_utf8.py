#!/usr/bin/python3
"""
This module contains a method that determines if a given
data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Method to determine if the data set is a valid UTF-8 encoding.

    Args:
        data (List[int]): List of integers representing the data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    # Number of bytes in the current UTF-8 character
    n_bytes = 0

    for num in data:
        # Get the binary representation. We only need the last 8 bits.
        bin_rep = format(num, '#010b')[-8:]

        if n_bytes == 0:
            # Count the number of leading 1's
            for bit in bin_rep:
                if bit == '0':
                    break
                n_bytes += 1

            # 1 byte characters (0xxxxxxx) or invalid case
            if n_bytes == 0:
                continue

            # Invalid scenarios:
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # Continuation bytes must start with '10'
            if not (bin_rep[0] == '1' and bin_rep[1] == '0'):
                return False

        # We reduce the count of expected bytes.
        n_bytes -= 1

    # If the last character ends mid-sequence, it's invalid.
    return n_bytes == 0
