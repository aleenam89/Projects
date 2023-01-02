import sys

input = str(sys.argv[1])

def main(input):
    longest = max(input.split(' '), key=len)
    print ('The longest word is', longest.lower())

main(input)
