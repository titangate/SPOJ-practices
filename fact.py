def findzero(n):
	a=5
	r=0
	while n>=a:
		r+=n/a
		a*=5
	return r
r=[]
for i in range(int(raw_input())):
	r.append(findzero(int(raw_input())))
for i in r:print i