#!/usr/bin/env python2
from __future__ import with_statement, print_function
import sys
def readFile(fname):
	for x in range(int(fname)):
		F = open("devops.txt", "a")
		F.write(str(x))
		F.write('\n')
  		#print(x)

if __name__ == '__main__':
	fname = sys.argv[1]
	readFile(fname)
