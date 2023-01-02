import sys

x = int(sys.argv[1])

def main(x):
    first = []
    second = x + 4
    for i in range(5000, 8001):
        if i % x==0 and i % second==0:
            first.append(i)
    print(first)

main(x)
