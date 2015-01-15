
class num:

	teens=['eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
	tens=['ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninty']
	ones=['one','two','three','four','five','six','seven','eight','nine']
	bigs=['','thousand','million']

	def __init__(self):
		pass

	def numToString(self,n):
		str=""
		if n == 0:
			return "zero"
		if n < 0:
			return "negative " + self.numToString(-1 * n)
		count=0
		while n > 0:
			print "HERE"
			if n%1000 != 0:
				str = self.numberString(n%1000) + ' ' + num.bigs[count] + ' ' + str
			n/=1000
			count+=1
		
		return str

	def numberString(self,n):
		print n
		str = ""
		if n >= 100:
			i=n//100-1
			str+=num.ones[i] + ' hundred '
			n%=100
		if n >= 11 and n <=19:
			return str + num.teens[n-11]+ ' '
		elif n == 10 or n >=20:
			str+=num.tens[n/10-1]+ ' '
			n%=10

		if n>=1 and n<=9:
			str+= num.ones[n-1]

		return str


def main():
	sol=num()
	print sol.numToString(1099)


if __name__ == '__main__':
	main()	

