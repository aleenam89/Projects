import sys

OneDollarBill = int(sys.argv[1])
quarters = int(sys.argv[2])
dimes = int(sys.argv[3])
nickels = int(sys.argv[4])
pennies = int(sys.argv[5])



def change (OneDollarBill, quarters, dimes, nickels, pennies):
    x = (OneDollarBill * 100 + quarters * 25 + dimes * 10 + nickels * 5 + pennies)/100
    print(f'The total value of your change is ${x}')

change(OneDollarBill, quarters, dimes, nickels, pennies)
