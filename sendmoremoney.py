from itertools import permutations

smm = 'MSENDORLGY'
for n in permutations(xrange(10)):
	d = {}
	for i in xrange(10):
		d[smm[i]] = n[i]
	a=reduce(lambda a,b:a*10+d[b],'SEND',0)
	b=reduce(lambda a,b:a*10+d[b],'MORE',0)
	c=reduce(lambda a,b:a*10+d[b],'GOLD',0)
	x=reduce(lambda a,b:a*10+d[b],'MONEY',0)
	if d['M'] != 0 and a+b+c==x:
		print d,a,b,c,x