import sys

x = sys.argv[1]


def main(x):
    argument = set(x.lower())

    count = 0
    for vowel in 'aeiou':
        if vowel in argument:
            count += 1
    print (count)

main(x)
