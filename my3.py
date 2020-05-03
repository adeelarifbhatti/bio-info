#!/usr/bin/env python2
from __future__ import with_statement, print_function
import sys
import numpy as numpy
def readFile(fname):
	rangelist = []
	rangedict = {}
	with open(fname, 'r') as f:
		for line in f:
			rangelist.append(line)
		#print(rangelist)
		for elem in rangelist:
			l=elem.split('\t')
			rangedict[tuple((l[0],l[1]))]=elem
		#print(rangedict)
	inter2= open("inter2.bed","w+")
	inter2.write(str(rangelist)+'\n')
	print(rangedict)
	return rangedict
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
	print(rangeFile)
	#print(sbjctdict)
	print(type(sbjctdict))
	print(type(rangeFile))
	snps = set(rangeFile).difference(set(sbjctdict))
	return [rangeFile[snp] for snp in snps]

if __name__ == '__main__':
	fname = sys.argv[1]
	vcfFile = sys.argv[2]
	result=getSNPs(fname,vcfFile)

	with open('result.txt', 'w') as out:
		for snp in result:
			out.write(snp)

	print('number of SNPs found:', len(result))
	