
def read_file(file_name):
  f = open(file_name, "r")
  rotations = []
  for x in f:
    rotations.append(x.strip())
  f.close()
  return rotations

start_point = 50
rotations = read_file('input.txt')
current_position = start_point
zero_count = 0

for rotation in rotations:
  if rotation[0] == 'L':
    rotation_num = int(rotation.strip('L'))
    n = -1 * (rotation_num % 100)
  elif rotation[0] == 'R':
    rotation_num = int(rotation.strip('R'))
    n = rotation_num % 100
  
  current_position = current_position + n
  if current_position == 0:
    zero_count = zero_count + 1 

  if current_position < 0:
    if current_position != n: zero_count = zero_count + 1 
    current_position = 100 + current_position
  elif current_position > 99:
    if current_position != n: zero_count = zero_count + 1 
    current_position = current_position - 100

  zero_count = zero_count + abs(rotation_num // 100)

print(zero_count)
# Part 1: 1132
# Part 2: 6623

    