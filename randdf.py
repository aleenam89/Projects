import sys
import numpy as np
import pandas as pd

x = int(sys.argv[1])
y = int(sys.argv[2])

def main(x,y):
    np.random.seed(56)
    df = pd.DataFrame(np.random.randint(0,100,size=(x,y)))
    print(df)

main(x,y)
