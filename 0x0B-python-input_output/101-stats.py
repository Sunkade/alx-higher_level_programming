import sys
import signal

# Define global variables to store metrics
total_file_size = 0
status_code_counts = {}

# Define a function to print the metrics
def print_metrics():
    print(f"Total file size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        print(f"{code}: {status_code_counts[code]}")

# Define a function to handle the keyboard interruption (CTRL + C)
def signal_handler(sig, frame):
    print_metrics()
    sys.exit(0)

# Register the signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

# Process input line by line
line_count = 0
try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        if len(parts) >= 9:
            status_code = parts[-2]
            file_size = int(parts[-1])
            total_file_size += file_size
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
            else:
                status_code_counts[status_code] = 1
        
        if line_count % 10 == 0:
            print_metrics()
except KeyboardInterrupt:
    print_metrics()
    sys.exit(0)
