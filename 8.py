import math
def findfollowup(sequence,n):
	if len(set(sequence))==1:
		return [sequence[0]]*n
	else:
		diffs = map(lambda n:sequence[n+1]-sequence[n],range(len(sequence)-1))
		answer = [sequence[-1]]
		for e in findfollowup(diffs,n):
			answer[-1]+=e
			answer.append(answer[-1])
		answer.pop()
		return answer

for i in range(int(raw_input())):
	a,b = map(int,raw_input().split())
	l = map(int,raw_input().split())
	for i in findfollowup(l,b):
		print i,
	print ''