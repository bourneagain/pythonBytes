def sol(num):
	big = ["", "one thousand", "two thousand", "three thousand", "five thousand"]
	hundreds = ["", "one hundred", "two hundred", "three hundred", "four hundred", "five hundred", "six hundred", "seven hundred", "eight hundred", "nine hundred"];
	teens = ["", "eleven", "twelve", "thirteen", "forteen", "fifteen", "sixteen", "seventeen", "eighteen", "ninteen"];
	tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninty"];
	ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
	if num % 100 > 10 and num %100 < 20:
		return big[(num/1000)%10] + hundreds[(num/100)%10] +' '+ teens[(num%100)%10] 
	else:
		return big[(num/1000)%10] + hundreds[(num/100)%10] +' '+ teens[(num/10)%10] +' '+ ones[num%10]

print sol(3104)
