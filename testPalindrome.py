import random
def anagramPalindrome(word):
		for n in range(len(word)):
				tempx=[[i] for i in word]
				random.shuffle(tempx)
				checkPalin(tempx)
anagramPalindrome("hanna")
