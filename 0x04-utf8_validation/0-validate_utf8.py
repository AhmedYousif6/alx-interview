#!/usr/bin/env python3
""" task 0 module
"""


def validUTF8(data):
    """ validate data if its utf8
    """
    bytes_remaining = 0

    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:
        byte = byte & 0xFF

        if bytes_remaining == 0:
            if (byte & mask1) == 0:
                continue
            elif (byte & (mask1 >> 1)) == 0:
                bytes_remaining = 1
            elif (byte & (mask1 >> 2)) == 0:
                bytes_remaining = 2
            elif (byte & (mask1 >> 3)) == 0:
                bytes_remaining = 3
            else:
                return False
        else:
            if not (byte & mask1 and not (byte & mask2)):
                return False
            bytes_remaining -= 1

    return bytes_remaining == 0
