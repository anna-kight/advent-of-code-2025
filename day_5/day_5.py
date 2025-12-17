from curses.ascii import isspace
from doctest import Example


def read_file(file_name):
  f = open(file_name, "r")
  ranges = []
  ingredients = []
  for x in f:
    
    if '-' in x:
       ranges.append([int(r) for r in x.strip().split('-')])
    elif not x.isspace():
      ingredients.append(int(x.strip()))

  f.close()
  return ranges, ingredients

ranges, ingredients = read_file('input.txt')
num_available = 0
in_range = set()

for i in ingredients:
  for r in ranges:
    if i >= r[0] and i <= r[1]:
      num_available = num_available + 1
      break

print(num_available)

# Part 1: 782