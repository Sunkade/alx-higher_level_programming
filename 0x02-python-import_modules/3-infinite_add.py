#!/usr/bin/python3

import sys

if __name__ == "__main__":
    """Print the sum of all arguments."""
    total = 0
    for i in range(1, len(sys.argv)):
        total += int(sys.argv[i])
    print("{}".format(total))
