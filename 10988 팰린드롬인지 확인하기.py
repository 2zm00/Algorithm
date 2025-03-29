word = input()

def reverse_word(word):
	return word[::-1]

def check_palindrome(word):
	if word == reverse_word(word):
		print("1")
	else:
		print("0")

check_palindrome(word)
