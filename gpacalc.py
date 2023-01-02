import sys


a = sys.argv[1]
b = sys.argv[2]
c = sys.argv[3]
d = sys.argv[4]


dict = {'A':4.0, 'A-':3.66, 'B+':3.33, 'B':3.0, 'B-':2.66, 'C+':2.33, 'C':2.0, 'C-':1.66, 'D+':1.33, 'D':1.00, 'D-':.66, 'F':0.00}

def main(a, b, c, d):
    x = (dict[a.upper()] + dict[b.upper()] + dict[c.upper()] + dict[d.upper()])/4
    print(f'My GPA is {x:.2f}')

main(a, b, c, d)
