def solve(amount,currency):
	dp = {}
	for value,weight in currency:
		if weight in dp:dp[weight] = min(value,dp[weight])
		else:dp[weight]=value
	for i in xrange(amount):
		if i in dp:
			for value,weight in currency:
				newweight = i+weight
				if newweight>amount:continue
				if newweight in dp:
					
					dp[newweight] = min(dp[i]+value,dp[newweight])
				else:
					dp[newweight] = dp[i]+value
	if amount in dp:
		print "The minimum amount of money in the piggy-bank is "+str(dp[amount])+"."
	else:
		print "This is impossible."

for i in xrange(input()):
	start,end = map(int,raw_input().split())
	currency = []
	for n in xrange(input()):
		currency.append(tuple(map(int,raw_input().split())))
	solve(end-start,currency)