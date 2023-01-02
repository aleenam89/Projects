import sys

x = str(sys.argv[1])

def main(x):

    print(len(x.replace('.', '')))

main(x)
