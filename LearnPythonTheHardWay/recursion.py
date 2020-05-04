def listSum(numList):
	if len(numList) == 1:
		return numList[0]
	else:
		return  numList[0] + listSum(numList[1:])


a = [1,2,3,4,5,6,7]

print listSum(a)