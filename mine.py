def solve(m,n):
	n = max(m,n)
	c = 0
	while n>=2:
		c+=1
		if n%2==0:
			n/=2
		else:
			n=(n-1)/2
	print c

for i in range(input()):
	m,n=map(int,raw_input().split())
	solve(m,n)