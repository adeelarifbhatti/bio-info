#!/usr/bin/env python2

from __future__ import with_statement, print_function
import sys
import numpy as numpy
def readSNPfile(vcfFile):
	snplist = []
	with open(vcfFile, 'r') as f:
		for line in f:
			if line.startswith('#'):
				continue
			snplist.append(line)
		
	snpdict = {}
	for elem in snplist:
		l = elem.split('\t')
		#              POS 
		snpdict[tuple((l[1]))] = elem

	print(snpdict)
def readFile(fname):
		value1=numpy.loadtxt(fname, delimiter="\t",usecols=[1])
		value2=numpy.loadtxt(fname, delimiter="\t",usecols=[2])
		i=0
		while i < len(value1):
			print(numpy.arange(value1[i],value2[i]))
			i+=1
			
if __name__ == '__main__':
	fname = sys.argv[1]
	vcfFile = sys.argv[2]
	readFile(fname)
	readSNPfile(vcfFile)
	