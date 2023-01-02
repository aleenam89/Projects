import sys

x = sys.argv[1]

def main(x):
    capital = [i for i,s in enumerate(x) if s.isupper()]
    capital_length = len(capital)
    sum_indices = sum(capital)
    print(capital_length)
    print(sum_indices)

main(x)
