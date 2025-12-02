
from tabnanny import check
from tkinter import Checkbutton


def read_file(file_name):
  f = open(file_name, "r")
  ranges = f.readline().split(',')
  f.close()
  return ranges

def split_ranges(ranges):
  range_pairs = []
  for r in ranges:
    r = r.strip()
    range_pairs.append(r.split('-'))
  return range_pairs


ranges = split_ranges(read_file('input.txt'))
invalid_sum = 0

# Part 1
# loop over the ranges
    # for each range check the numbers that have an even number of digets 
    # for those to string split in half and check if equal

for r in ranges:
  for id in range(int(r[0]), int(r[1]) + 1):
    id_str = str(id)
    len_id = len(id_str)
    # if len(id_str) % 2 == 0: # part 1
    #     first_half, second_half = id_str[:len(id_str)//2 + len(id_str)%2], id_str[len(id_str)//2 + len(id_str)%2:]
    #     if first_half == second_half:
    #       invalid_sum = invalid_sum + id
    for seq_len in range(1, len_id//2 +1): # part 2
       if len_id % seq_len == 0:
          check_seq = id_str[0:seq_len]
          if id_str == check_seq*(len_id//seq_len):
             invalid_sum = invalid_sum + id
             break

print(invalid_sum)


def repeat(string):
    l = len(string)
    for i in range(1, len(string)//2+1):
        if l%i: continue
        s = string[0:i]
        if s*(l//i) == string:
            return s


# Part 1: 19128774598
# Part 2: 21932258645