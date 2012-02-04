validdigit = map(str,xrange(10,27))
try:
	def solve(n):
		depth = 0
		count = 0
		for c in n:
			if c=='{':
				depth+=1
			if c=='}':
				if depth<=0:
					count +=1
					depth -=1
		count += l(depth/2)
		
		return count
except:pass
n = raw_input()
while n[0]!='-':
	print '1. '+ str(solve(n))
	n=raw_input()