#!/usr/bin/env python2
import numpy as numpy 
import pandas as pandas
import sys
a=numpy.array((1,2,3,4),float)
print(a)
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
	print("From varientmethod")
	varientArray = numpy.asarray(varientlist) 
	print(varientArray)
	return varientArray

def readFile(fname):
	rangelist = []
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
		'''
		df=pandas.DataFrame(a)
		
		for x in range(10):
			print(df[x])
		'''
		print("Above is the DF ")
		print(a)
		print("Above is a ")
		return a
if __name__ == '__main__':
	fname = sys.argv[1]
	vcffile= sys.argv[2]
	result=readFile(fname)
	#makeVariantArray(vcffile)
	print(numpy.intersect1d(makeVariantArray(vcffile),readFile(fname)))

	with open('result.txt', 'w') as out:
		for snp in result:
			out.write(str(snp))

	print('number of SNPs found:', len(result))