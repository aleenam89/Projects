import sys

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

def main(a,b,c):
    discriminant = b**2 - 4*a*c
    x = (-b + discriminant**0.5)/(2*a)
    y = (-b - discriminant**0.5)/(2*a)
    print (f'The solutions are {x:.2f} and {y:.2f}')

main(a,b,c)
