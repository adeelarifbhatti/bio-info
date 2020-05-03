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
	rangelist = []
	with open(fname, 'r') as f:
		for line in f:
			if line.startswith('#'):
				continue
			rangelist.append(line)
			rangedict = {}
		for elem in rangelist:
			l = elem.split('\t')
			#              POS 
			rangedict[tuple((l[0],l[1]))] = elem

		return rangedict
		#while i < len(value1):
		#return dict(enumerate(numpy.arange(value1[i],value2[i]).flatten(), 1))
		print(value1)
		value1.tolist()
		rangeDict = {}
		for elem in value1:
			l = elem.split('\t')
			#              CHR  Start
		#	rangeDict[tuple((l[0],l[1]))] = elem
		
		
		#	i+=1			
if __name__ == '__main__':
	fname = sys.argv[1]
	vcfFile = sys.argv[2]
	result=getSNPs(fname,vcfFile)

	with open('result.txt', 'w') as out:
		for snp in result:
			out.write(snp)

	print('number of SNPs found:', len(result))
	