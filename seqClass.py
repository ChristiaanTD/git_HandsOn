#!/usr/bin/env python3

import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args() 

args.seq= args.seq.upper()
if re.search('^[ACGTU]+$', args.seq):
    if re.search('T', args.seq) and not re.search('U', args.seq): #Ensure T exclusivity
        print ('The sequence is DNA')
    elif re.search('U', args.seq) and not re.search('T', args.seq): #Ensure U exclusivity
        print ('The sequence is RNA')
    elif re.search('T', args.seq) and re.search('U', args.seq): #In case both are present print an error message.
        print ('ERROR: The sequence contains both T and U')
    else: #for other sequences that could be DNA or RNA (for example AGGAGAG) print that both are possible
        print ('The sequence can be DNA or RNA')
else: #for the rest print that its neither DNA or RNA
    print ('The sequence is not DNA nor RNA')

if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq):
        print("MOTIF FOUND")

    else:
        print("MOTIF NOT FOUND")


