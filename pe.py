from collections import deque
background = 'xx..xx....xx..xx'	
def receive():
	return raw_input()[:4]+raw_input()[:4]+raw_input()[:4]+raw_input()[:4]+raw_input()[:0]

def convert(puzz):
    ret = ""
    for i in range(len(puzz)):
        if puzz[i] == ' ': ret += ' '
        elif i in [0, 1, 4, 5, 10, 11, 14, 15]:
            if puzz[i] == 'x': ret += '.'
            else: ret += 'x'
        else:
            if puzz[i] == 'x': ret += 'x'
            else: ret += '.'
    return ret


def flip(p):
	l=''
	for i in xrange(4):
		x=p[0+i]+p[4+i]+p[8+i]+p[12+i]
		l+=x
	return l

def expand(p):
	transp = flip(p)
	n = p.find(' ')
	r = set()
	x,y = n%4,n/4
	# tip 
	r.add(p[:y*4]+' '+p[y*4:n]+p[n+1:])
	r.add(p[:n]+p[n+1:y*4+4]+' '+p[y*4+4:])
	
	r.add(convert(transp[:y*4]+' '+transp[y*4:n]+transp[n+1:]))
	r.add(convert(transp[:n]+transp[n+1:y*4+4]+' '+transp[y*4+4:]))
	
	# move along outer ring
	if x in [0,3]:
		for i in (0,x):
			# move to the right
			r.add(p[:n-i]+' '+p[n-i+1:n]+p[n+1:])
		for i in (x,4):
			# to the left
			r.add(p[:n-i]+p[n-i+1:n]+' '+p[n+1:])
	return r
r = [1,2,3,-1,-2,-3]
def dfs(p,target):
	d=deque()
	d.append((p,0))
	visited = {}
	solved = False
	visited[p] = True
	while len(d)>0:
		if solved:return
		m = d.popleft()
		p,depth=m
		for i in r:
			p2=hozop(p,i)
			if p2!=False and p2 not in visited:
				if p2 in target:
					print depth+1
					solved = True
					break
				d.append((p2,depth+1))
				visited[p2] = True
			p2=vertop(p,i)
			if p2!=False and p2 not in visited:
				if p2 in target:
					print depth+1
					solved = True
					break
				d.append((p2,depth+1))
				visited[p2] = True
			#print d
	print 'Impossible.'
#try:
if True:
	while True:
		p = convert(receive())
		target = list(convert(receive()))
		t = []
		for i in xrange(16):
			if target[i]=='.':
				ori = target[i]
				target[i]=' '
				t.append(''.join(target))
				target[i] = ori
		print expand(p),p
#except:pass
