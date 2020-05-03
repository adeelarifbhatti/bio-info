#!/usr/bin/env python2
from __future__ import with_statement, print_function
import sys
def readFile():
	file = open("intervals.bed","r")
	for line in file:
  		fields = line.split("\t")
  		chromosome = fields[0]
  		start = fields[1]
  		stop = fields[2]
  		print(chromosome +'\t'+ start+ '\t'+ stop)
  		F = open("devops.txt", "a")
		for x in range(int(start), int(stop)):
			F = open("devops.txt", "a")
			F.write(chromosome+'\t'+str(x)+'\t'+'\n')
		F.close()
			#F.write('\n')
if __name__ == '__main__':
	readFile()
