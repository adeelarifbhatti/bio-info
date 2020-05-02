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
		snpdict[tuple((l[0],l[1]))] = elem

	return snpdict

def getSNPs(varientRange, sbjctlist):
	sbjctdict = readSNPfile(sbjctlist)
	rangeFile = readFile(varientRange)


	# This returns dict keys that are in sbjctdict but not in ctrldict
	print(rangeFile)
	#print(sbjctdict)
	print(type(sbjctdict))
	print(type(rangeFile))
	#print(sbjctdict)
	snps = set(sbjctdict).difference(set(rangeFile))
	return [sbjctdict[snp] for snp in snps]

def readFile(fname):
		value1=numpy.loadtxt(fname, delimiter="\t",usecols=[1])
		value2=numpy.loadtxt(fname, delimiter="\t",usecols=[2])
		i=0
		#while i < len(value1):
		return dict(enumerate(numpy.arange(value1[i],value2[i]).flatten(), 1))
		
		#	i+=1			
if __name__ == '__main__':
	fname = sys.argv[1]
	vcfFile = sys.argv[2]
	result=getSNPs(fname,vcfFile)

	with open('result.txt', 'w') as out:
		for snp in result:
			out.write(snp)

	print('number of SNPs found:', len(result))
	