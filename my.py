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

	#print(snpdict.keys())
	#print(type(snpdict.keys()))
	return snpdict



def getSNPs(varientRange, sbjctlist):
	sbjctdict = readSNPfile(sbjctlist)
	rangeFile = readSNPfile(varientRange)


	# This returns dict keys that are in sbjctdict but not in ctrldict
	#print(rangeFile)
	#print(sbjctdict)
	print(type(sbjctdict))
	print(type(rangeFile))
	#print(sbjctdict)
	snps = set(sbjctdict).difference(set(rangeFile))
	return [sbjctdict[snp] for snp in snps]

def readFile(fname):
		#value1=numpy.loadtxt(fname, delimiter="\t",usecols=[0])	
		value2=numpy.loadtxt(fname, delimiter="\t",usecols=[1])
		value3=numpy.loadtxt(fname, delimiter="\t",usecols=[2])
		i=0
		#while i < len(value1):
		#a=(dict(enumerate(numpy.arange(value2[i],value3[i]).flatten())))
		#return dict(enumerate(numpy.arange(value1[i],value2[i]).flatten()))
		rangelist = numpy.arange(value2[i],value3[i]).tolist()
		#a=dict(enumerate(rangelist).flatten())
		a=str(rangelist)
		print(type(a))
		print(rangelist)
		print(type(rangelist))
		rangedict = {}
		'''
		for elem in rangelist:
			l = elem
			#              POS 
			rangedict[tuple((l[0]))] = elem
		'''
		print(rangedict)
		#return rangelist
		return dict(enumerate(numpy.arange(value1[i],value2[i]).flatten()))
		
		#	i+=1			
if __name__ == '__main__':
	fname = sys.argv[1]
	vcfFile = sys.argv[2]
	result=getSNPs(fname,vcfFile)

	with open('result.txt', 'w') as out:
		for snp in result:
			out.write(snp)

	print('number of SNPs found:', len(result))
	