import sys
import string

x = str(sys.argv[1])

def main(x):
    a = x.translate(str.maketrans('','', string.punctuation)).lower().strip().replace(" ", "")
    palindrome = a [::-1]
    if palindrome == a:
        print("It's a palindrome!")
    else:
        print("It's not a palindrome!")

main(x)
