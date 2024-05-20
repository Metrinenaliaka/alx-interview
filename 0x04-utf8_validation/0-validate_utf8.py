#!/usr/bin/python3


def validUTF8(data):
    """
    Checks if the data set represents a valid UTF-8 encoding
    """
    # Number of bytes in the current character
    num_bytes = 0

    # Iterate through each integer in the data set
    for num in data:
        # Check if the current byte is a continuation byte
        if num & 0b11000000 == 0b10000000:
            # If it's not a valid continuation byte, return False
            if num_bytes == 0:
                return False
            # Decrement the number of bytes remaining
            num_bytes -= 1
        else:
            # Check the number of bytes required for the current character
            if num_bytes > 0:
                return False
            # Determine the number of bytes required based on the first byte
            if num & 0b10000000 == 0:
                num_bytes = 0
            elif num & 0b11100000 == 0b11000000:
                num_bytes = 1
            elif num & 0b11110000 == 0b11100000:
                num_bytes = 2
            elif num & 0b11111000 == 0b11110000:
                num_bytes = 3
            else:
                return False

    # If there are remaining bytes, return False
    if num_bytes > 0:
        return False

    # All checks passed, return True
    return True
