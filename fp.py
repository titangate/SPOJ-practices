import math
table = None
def newseq(s,remainder):
	seq=s[:]
	i=0
	while table[remainder][i] in seq:i+=1
	n = table[remainder][i]
	i=0
	while True:
		if i==len(seq):
			seq.insert(i-1,n)
			break
		elif i==len(seq)-1:
			if seq[0]>n:
				seq.append(n)
			else:
				seq.insert(0,n)
			break
		else:
			
			exist = str(seq[i])+str(seq[i+1])
			
			nn = n*10.0**(len(exist)-len(str(n)))
			print exist,nn
			if int(exist) < nn:
				seq.insert(i,n)
				break
			else:
				i+=1
	return seq
def sumstring(s):
	return int(reduce(lambda a,b:a+str(b),s))
for case in xrange(input()):
	n,k=map(int,raw_input().split())
	table = [[]]*9
	for i in xrange(n):
		number=input()
		table[number%9].append(number)
	for t in table:t.sort(reverse=True)
	dp=map(lambda x:[[]]*9,xrange(k))
	for i in xrange(9):
		seq = newseq([],i)
		amt = sumstring(seq)
		dp[0][i]=(seq,amt)
	for i in xrange(1,k):
		for j in xrange(9):
			maxseq,maxamt = dp[i-1][0]
			maxseq = newseq(maxseq,j%9)
			maxamt = sumstring(seq)
			for k in xrange(1,9):
				nseq,namt = dp[i-1][k]
				nseq = newseq(maxseq,j%9)
				namt = sumstring(seq)
				if namt>maxamt:
					maxseq,maxamt=nseq,namt
			dp[i][j]=(maxseq,maxamt)
	print dp