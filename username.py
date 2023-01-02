import sys

first_name = sys.argv[1]
last_name = sys.argv[2]

def main(first_name, last_name):
    username= first_name[0].lower() + last_name[-7:].lower()+ (str(len(first_name)+len(last_name)))
    print('Your username is', username)

main(first_name,last_name)
