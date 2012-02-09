from collections import deque
background = 'xx..xx....xx..xx'	
def receivepiece():
	bg = ''
	for i in xrange(4):
		line=raw_input()
		bg+=line
	s = bg.index(' ')
	bg = filt(bg)
	bg = bg[:s]+' '+bg[s+1:]
	return bg,s
def receivetarget():
	bg = ''
	for i in xrange(4):
		line=raw_input()
		bg+=line
	return bg

def filt(config):
	state = ''
	for i in xrange(16):
		if config[i]==' ':state+='.'
		elif background[i]==config[i]:state+='.'
		else:state+='x'
	return state

def hozop(p,start,shift):
	m,y = start%4,start/4
	if m+shift>3 or m+shift<0:return False,-1
	if shift<0:
		start = start + shift
		shift = -shift
	
	if (y==1 or y==2) and shift<3:return False,-1
	return p[:start]+p[start+1:start+shift+1]+p[start]+p[start+shift+1:],start
def flip(p):
	l=''
	for i in xrange(4):
		x=p[0+i]+p[4+i]+p[8+i]+p[12+i]
		l+=x
	return l

def vertop(p,start,shift):
	start = (start%4)*4+start/4
	a,start=hozop(flip(p),start,shift)
	if a==False:return a,-1
	p = flip(a)
	return p,(start%4)*4+start/4


r = [1,2,3,-1,-2,-3]
def dfs(p,start):
	d=deque()
	d.append((p,start,0))
	visited = {}
	solved = False
	visited[p] = True
	while len(d)>0:
		if solved:return
		m = d.popleft()
		p,s,depth=m
		for i in r:
			p2,s2=hozop(p,s,i)
			if p2!=False and p2 not in visited:
				if filt(p2)==target:
					print depth+1
					solved = True
					break
				d.append((p2,s2,depth+1))
				visited[p2] = True
			p2,s2=vertop(p,s,i)
			if p2!=False and p2 not in visited:
				if filt(p2)==target:
					print depth+1
					solved = True
					break
				d.append((p2,s2,depth+1))
				visited[p2] = True
			#print d
	print 'Impossible.'
#try:
if True:
	while True:
		p,start = receivepiece()
		raw_input()
		target = receivetarget()
		raw_input()
		dfs(p,start)
#except:pass