# function to print instructions
def game_instructions():
  file2 = open('instructions.txt', 'r')
  inst = file2.read()
  print(inst)
  file2.close()