import sys

celsius = float(sys.argv[1])

def main(celsius):
    fahrenheit = celsius * 1.8 + 32
    print(f'The temperature is {fahrenheit:.2f} degrees Fahrenheit.')

main(celsius)
