from collections import deque
background = 'xx..xx....xx..xx'	
def receivepiece():
	bg = ''
	for i in xrange(4):
		line=raw_input()
		bg+=line
	return bg,bg.index(' ')

def filt(config):
	state = ''
	for i in xrange(16):
		if config[i]==' ':state+='.'
		elif background[i]==config[i]:state+='.'
		else:state+='x'

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
	p,start= flip(hozop(flip(p),start,shift))
	return p,(start%4)*4+start/4

p,start = receivepiece()

def dfs(p,start):
	d=deque((p,start,0))
	while len(d)>0:
		p,s,depth=d.popleft()
		p2,s2=hozop(p,s,1)
		if p2!=False:
			if 
			d.push((p2,s2,depth+1))
