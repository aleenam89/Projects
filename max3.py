import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])


def main(x,y,z):
    if x>y and x>z:
        print(x)
    elif y>x and y>z:
        print(y)
    else:
        print(z)

main(x,y,z)
