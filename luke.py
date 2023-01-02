import sys


relations = {'Darth Vader':'father', 'Leia':'sister', 'Han':'brother in law', 'R2D2':'droid', 'Rey':'Padawan', 'Tatooine':'homeworld'}


def Luke():

    if sys.argv[1] == 'Darth Vader':
        print("No, I am your father")
    else:
        print('Luke, i am your', relations[sys.argv[1]])

Luke()
