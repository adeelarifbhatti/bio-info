#!/usr/bin/env python2
import numpy as numpy 
import sys
def makeVariantArray(vcffile):
	snplist = []
	varientlist=[]
	with open(vcffile, 'r') as f:
		for line in f:
			if line.startswith('#'):
				continue
			snplist.append(line)

	for elem in snplist:
		l = elem.split('\t')
		#       POS   ALT
		varientlist.append(l[1])
	#print("From varientmethod")
	varientArray = numpy.asarray(varientlist) 
	#print(varientArray)
	return varientArray
def readFile(fname):
	rangelist = []
	result2=0
	b = []
	with open(fname, 'r') as f:
		for line in f:
			if line.startswith('#'):
				continue
			rangelist.append(line)
			rangedict = {}
		for elem in rangelist:
			fields = elem.split('\t')
			chromosome = fields[0]
  			start = fields[1]
  			stop = fields[2]
			a=[numpy.arange(int(start),int(stop))]
			##b=a
			result=numpy.intersect1d(vcffiles,a)
			print('Number of Variants in Interval' ,fields[1] ,'and',fields[2],' is ', len(result))
			result2 += len(result)

		print('"""""""""""Total Number of Variants are:"""""""""""""', result2)
		return b
if __name__ == '__main__':

	fname = sys.argv[1]
	vcffile= sys.argv[2]
	vcffile2=sys.argv[3]
	vcffiles=numpy.append(makeVariantArray(vcffile),makeVariantArray(vcffile2))
	readFile(fname)

	