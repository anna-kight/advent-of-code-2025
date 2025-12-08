def read_file(file_name):
  f = open(file_name, "r")
  diagram = []
  for x in f:
    diagram.append(list(x.strip()))
  f.close()
  return diagram

def get_num_adj(diagram, location):
  num_adj = 0
  if location[0] > 0:
    if diagram[location[0] - 1][location[1]] in ['@', 'x']: #Directly above 
      num_adj = num_adj + 1
    if location[1] > 0 and diagram[location[0] - 1][location[1] - 1] in ['@', 'x']: #Up and to the left
      num_adj = num_adj + 1
    if location[1] < len(diagram[0]) - 1 and diagram[location[0] - 1][location[1] + 1] in ['@', 'x']: #Up and to the right
      num_adj = num_adj + 1

  if location[0] < len(diagram) - 1:
    if diagram[location[0] + 1][location[1]] in ['@', 'x']: #Directly below 
      num_adj = num_adj + 1
    if location[1] > 0 and diagram[location[0] + 1][location[1] - 1] in ['@', 'x']: #Down and to the left
      num_adj = num_adj + 1
    if location[1] < len(diagram[0]) - 1 and diagram[location[0] + 1][location[1] + 1] in ['@', 'x']: #Down and to the right
      num_adj = num_adj + 1

  if location[1] > 0 and diagram[location[0]][location[1] - 1] in ['@', 'x']: #Directly to the left
      num_adj = num_adj + 1
 
  if location[1] < len(diagram[0]) - 1 and diagram[location[0]][location[1] + 1] in ['@', 'x']: #Directly to the right
      num_adj = num_adj + 1
      
  return num_adj
  
def get_and_remove_num_accessable(diagram):
  accessable = 0
  for i in range(len(diagram)):
    for j in range(len(diagram[0])):
      if diagram[i][j] in ['@', 'x'] and get_num_adj(diagram, [i,j]) < 4:
       accessable = accessable + 1
       diagram[i][j] = 'x'
  return accessable, diagram


updated_diagram = read_file('input.txt')

accessable = 1
removable = 0 

while accessable > 0:

    accessable, diagram = get_and_remove_num_accessable(updated_diagram)
    removable = removable + accessable

    updated_diagram = []
    for row in diagram:
      updated_diagram.append([p.replace('x', '.') for p in row])



print(removable)

# Part 1: 1384
# Part 2: 8013