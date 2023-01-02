import sys
import numpy as np

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

def main(x,y,z):
    if z > x:
        pass
    else:
        np.random.seed(42)
        a = np.random.randint(0,10,size=x)
        b = a*y
        c = b[z]
        print('Your random value is', c)


main(x,y,z)
