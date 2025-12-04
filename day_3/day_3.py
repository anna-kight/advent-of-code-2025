def read_file(file_name):
  f = open(file_name, "r")
  banks = []
  for x in f:
    banks.append(x.strip())
  f.close()
  return banks

banks  = read_file('input.txt')
total_joltage = 0

for bank in banks:
  int_bank = [int(b) for b in list(bank)]
# Part 1: Find max that isn't at the end then find the max after that including the end
#   first_dig_index = int_bank.index(max(int_bank[0:len(int_bank)-1]))
#   second_dig_index = int_bank.index(max(int_bank[first_dig_index+1:]))
#   max_joltage = int(bank[first_dig_index] + bank[second_dig_index])

# Part 2: Find the max that is not in the last 11 then find the max that isn't in the last 10... until you have 12 numbers
  prev_dig_index = -1
  next_dig_index = 0
  max_joltage_str = ''
  for i in reversed(range(12)): #11, 10...0 find max excluding last i numbers 
    next_dig_index = prev_dig_index + 1 + int_bank[prev_dig_index + 1: len(int_bank) - i].index(max(int_bank[prev_dig_index + 1: len(int_bank) - i]))
    max_joltage_str = max_joltage_str + bank[next_dig_index]
    prev_dig_index = next_dig_index

  total_joltage = total_joltage + int(max_joltage_str)

print(total_joltage)

# Part 1: 16842
# Part 2: 167523425665348