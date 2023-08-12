#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of argumnents."""
    import sys

    count = len(sys.argv) - 1

    if count == 0:
        print("0 arguments.")
   elif count == 1:
        print ("1 argument:")
   else:
        print("{} arguments:".format(count))

   for r in range(count):
            print("{}: {}".format(r + 1, sys.argv[r + 1]))
