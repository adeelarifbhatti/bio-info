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
		snpdict[tuple((l[0],l[1]))] = elem
	return snpdict
def getSNPs(sbjctlist):
	sbjctdict = readSNPfile(sbjctlist)
	rangeFile = readSNPfile("intervalrange.txt")
	print(type(sbjctdict))
	print(type(rangeFile))
	#print(sbjctdict)
	snps = set(sbjctdict).difference(set(rangeFile))
	return [sbjctdict[snp] for snp in snps]
def readFile():
	file = open("intervals.bed","r")
	for line in file:
  		fields = line.split("\t")
  		chromosome = fields[0]
  		start = fields[1]
  		stop = fields[2]
  		print(chromosome +'\t'+ start+ '\t'+ stop)
  		F = open("intervalrange.txt", "a")
		for x in range(int(start), int(stop)):
			F = open("intervalrange.txt", "a")
			F.write(chromosome+'\t'+str(x)+'\t'+'\n')
		F.close()			
if __name__ == '__main__':
	vcfFile = sys.argv[1]
	readFile()
	result=getSNPs(vcfFile)

	with open('result.txt', 'w') as out:
		for snp in result:
			out.write(snp)

	print('number of SNPs found:', len(result))
	