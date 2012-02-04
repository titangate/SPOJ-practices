#shellgame
d = {
'left' : False,
'center' : False,
'right' : False
}

d[raw_input()] = True
for i in xrange(input()):
	a,b = raw_input().split()
	d[a],d[b]=d[b],d[a]

for k,v in d.iteritems():
	if v:
		print k