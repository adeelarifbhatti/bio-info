#!/usr/bin/env python2
import numpy as numpy 
import sys
def vcfFunction(vcffile):
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
	#print(varientlist)
	return varientlist
def intervalFile(Argument1):
	rangelist = []
	rangelist2= []
	with open(Argument1, 'r') as f:
		for line in f:
			if line.startswith('#'):
				continue
			rangelist.append(line)
		for elem in rangelist:
			fields = elem.split('\t')
  			start = fields[1]
  			stop = fields[2]
			a=numpy.arange(int(start),int(stop)).tolist()
			rangelist2.extend(a)
		print(len(rangelist2))
		return rangelist2
if __name__ == '__main__':
	Argument1 = sys.argv[1]
	vcf= sys.argv[2]
	vcf2=sys.argv[3]
	vcffiles=numpy.append(vcfFunction(vcf),vcfFunction(vcf2))
	result=numpy.intersect1d(vcffiles,intervalFile(Argument1))
	with open('result.txt', 'w') as out:
		for snp in result:
			out.write(str(snp)+'\n')
	print('number of SNPs found:', len(result))