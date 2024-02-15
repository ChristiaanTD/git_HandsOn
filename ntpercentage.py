import sys
from argparse import ArgumentParser

# Set up parser variable and add seq argument to it.
parser = ArgumentParser(description='Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type=str, required=True, help="Input sequence")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

# Set args as the output of the parser script
args = parser.parse_args()
# Convert to uppercase
args.seq = args.seq.upper()

# Check if sequence contains non DNA/RNA letters
if any(letter not in 'ACGTU' for letter in args.seq):
    print('ERROR: The sequence contains non-DNA/RNA letters.')
    sys.exit(1)

# Check if sequence contains U and T simultaneously
if 'T' in args.seq and 'U' in args.seq:
    print('ERROR: The sequence contains both T and U.')
    sys.exit(1)

# Set up count variables
Ucount = 0
Tcount = 0
Acount = 0
Gcount = 0
Ccount = 0

# Check if the sequence contains non-DNA/RNA letters
if any(letter not in 'ACGTU' for letter in args.seq):
    print('ERROR: The sequence contains non-DNA/RNA letters.')
    sys.exit(1)

sequence_length = len(args.seq)

# Set up loop to check the letters and increase count per letter
for letter in args.seq:
    if letter == 'U':
        Ucount += 1
    elif letter == 'T':
        Tcount += 1
    elif letter == 'A':
        Acount += 1
    elif letter == 'G':
        Gcount += 1
    elif letter == 'C':
        Ccount += 1

if Ucount > 0 and Tcount == 0:
    print('The sequence is RNA')
    print(f'%U: {(Ucount / sequence_length) * 100:.2f}%')
    print(f'%G: {(Gcount / sequence_length) * 100:.2f}%')
    print(f'%C: {(Ccount / sequence_length) * 100:.2f}%')
    print(f'%A: {(Acount / sequence_length) * 100:.2f}%')

elif Ucount == 0 and Tcount > 0:
    print('The sequence is DNA')
    print(f'%T: {(Tcount / sequence_length) * 100:.2f}%')
    print(f'%G: {(Gcount / sequence_length) * 100:.2f}%')
    print(f'%C: {(Ccount / sequence_length) * 100:.2f}%')
    print(f'%A: {(Acount / sequence_length) * 100:.2f}%')
