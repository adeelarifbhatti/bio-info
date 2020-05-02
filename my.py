#!/usr/bin/env python2

from __future__ import with_statement, print_function
import sys
import numpy as numpy



def readFile(fname):

	#snplist = []
	#with open(fname, 'r') as f:
	#	for line in f:
	#		if line.startswith('#'):
	#			continue
	#		snplist.append(line)
	#	for i in snplist:
	#		arr=numpy.array(snplist)
		#print(snplist)

		#print(arr)
		##for i in range(len(snplist)):
		##	x=(snplist[i])

		value1=numpy.loadtxt(fname, delimiter="\t",usecols=[1])
		value2=numpy.loadtxt(fname, delimiter="\t",usecols=[2])
		#a=numpy.arange(data[:,0],data[:,1])
		#print(a)
		#array3=value1[numpy.array(0)]
		#print(len(data))
		#print(value1[0])
		i=0
		while i < len(value1):
			print(numpy.arange(value1[i],value2[i]))
			i+=1
			

		

if __name__ == '__main__':
	fname = sys.argv[1]
	readFile(fname)
	