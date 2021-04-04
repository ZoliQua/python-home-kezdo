
import argparse

parser = argparse.ArgumentParser(prog = 'top',
								 description = 'Show top lines from the file')

parser.add_argument('-l', '--lines', type=int, default=10)

args = parser.parse_args()

# Usage python test-argparse-lib.py --lines=5 data/lotto/source/otos.csv