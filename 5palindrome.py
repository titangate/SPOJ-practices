def findPalindrome(sn):
	if len(sn)%2==0:
		firsthalf = sn[:len(sn)/2]
		lasthalf = sn[len(sn)/2:]
		if int(lasthalf)<int(firsthalf[::-1]):
			print firsthalf+firsthalf[::-1]
		elif len(str(int(firsthalf)+1))>len(firsthalf):
			print str(int(firsthalf)+1)+str(int(firsthalf)+1)[1::-1]
		else:
			print str(int(firsthalf)+1)+str(int(firsthalf)+1)[::-1]
	else:
		firsthalf = sn[:len(sn)/2]
		lasthalf = sn[len(sn)/2+1:]
		middigit = sn[len(sn)/2]
		if int(lasthalf)<int(firsthalf[::-1]):
			print firsthalf+middigit+firsthalf[::-1]
		elif len(str(int(firsthalf+middigit)+1))>len(firsthalf+middigit):
			print '1'+'0'*(len(sn)-1)+'1'
		else:
			print firsthalf+str(int(middigit)+1)+(firsthalf)[::-1]

for i in range(int(raw_input())):
	findPalindrome(raw_input())