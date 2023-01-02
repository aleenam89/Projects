import sys
import numpy as np

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
d = int(sys.argv[4])

def main(a,b,c,d):
    print(type(np.array([a,b,c,d])))
    print(a*b*c*d)

main(a,b,c,d)
