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
		#snpdict[tuple((l[1]))] = elem
		snpdict[l[1]] = elem
	print(snpdict.keys())
	print(type(snpdict.keys()))
	return snpdict



def getSNPs(varientRange, sbjctlist):
	sbjctdict = readSNPfile(sbjctlist)
	rangeFile = readFile(varientRange)


	# This returns dict keys that are in sbjctdict but not in ctrldict
	#print(rangeFile)
	#print(sbjctdict)
	dictOfWords = { i : 5 for i in rangeFile }
	print(type(sbjctdict.keys()))
	print(type(sbjctdict))
	print(type(dictOfWords.keys()))
	print(dictOfWords.values())
	#print(sbjctdict)
	snps = set(sbjctdict.keys()).difference(set(dictOfWords.values()))
	#snps = set(sbjctdict.keys())-(set(dictOfWords.keys()))
	return [sbjctdict[snp] for snp in snps]

def readFile(fname):
		#value1=numpy.loadtxt(fname, delimiter="\t",usecols=[0])	
		value2=numpy.loadtxt(fname, delimiter="\t",usecols=[1])
		value3=numpy.loadtxt(fname, delimiter="\t",usecols=[2])
		i=0
		#while i < len(value1):
		#a=(dict(enumerate(numpy.arange(value2[i],value3[i]).flatten())))
		#return dict(enumerate(numpy.arange(value1[i],value2[i]).flatten()))
		rangelist = numpy.arange(value2[i],value3[i],1, dtype=int).tolist()
		#a=dict(enumerate(rangelist).flatten())
		print(rangelist)
		print(type(rangelist))
		#dictOfWords = { i : 5 for i in rangelist }
		#print(dictOfWords.keys())
		#print(type(dictOfWords))

		return rangelist
		
		#	i+=1			
if __name__ == '__main__':
	fname = sys.argv[1]
	vcfFile = sys.argv[2]
	result=getSNPs(fname,vcfFile)

	with open('result.txt', 'w') as out:
		for snp in result:
			out.write(snp)

	print('number of SNPs found:', len(result))
	