import numpy as numpy 
#from thread import start_new_thread
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
def readFile(fname,i,j):	
	rangelist = []
	global final 
	result2=0
	b = []
	with open(fname, 'r') as f:
		for line in f:
			if line.startswith('#'):
				continue
			rangelist.append(line)
		for x in range(i,j):
			fields = rangelist[x].split('\t')
			#print(x)
			chromosome = fields[0]
  			start = fields[1]
  			stop = fields[2]
			a=[numpy.arange(int(start),int(stop))]
			##b=a
			result=numpy.intersect1d(vcffiles,a)
			print('Number of Variants in Interval' ,fields[1] ,'and',fields[2],' is ', len(result))
			result2 += len(result)
		final += result2
if __name__ == '__main__':
	fname = sys.argv[1]
	vcffile= sys.argv[2]
	vcffile2=sys.argv[3]
	final=0
	vcffiles=numpy.append(makeVariantArray(vcffile),makeVariantArray(vcffile2))
	readFile(fname,0,8)
	print('"""""""""""Total Number of Variants are:"""""""""""""', final)

	

	
