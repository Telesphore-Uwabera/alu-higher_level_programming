import sys
from collections import defaultdict

# Initialize variables
total_size = 0
status_code_counts = defaultdict(int)
line_count = 0

try:
    for line in sys.stdin:
        # Parse input line
        parts = line.split()
        ip_address = parts[0]
        status_code = parts[8]
        file_size = parts[9]
        total_size += int(file_size)
        status_code_counts[status_code] += 1
        line_count += 1

        # Print metrics every 10 lines
        if line_count % 10 == 0:
            print(f'Total file size: {total_size}')
            for code in sorted(status_code_counts.keys()):
                print(f'{code}: {status_code_counts[code]}')

except KeyboardInterrupt:
    # Print final metrics
    print(f'Total file size: {total_size}')
    for code in sorted(status_code_counts.keys()):
        print(f'{code}: {status_code_counts[code]}')
