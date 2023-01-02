import sys
import pandas as pd

df = pd.read_csv('president_heights.csv')

x = int(sys.argv[1])
y = int(sys.argv[2])

def main(x,y):
    slice =  df.iloc[x:y,1].mean(axis=0)
    print(f'The average height of presidents number {x} to {y} is {slice:.2f}')


main(x,y)
