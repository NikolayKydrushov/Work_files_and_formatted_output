
from pprint import pprint

name = 'name.txt'
file = open(name, 'r')
pprint(file.read())
file.close()