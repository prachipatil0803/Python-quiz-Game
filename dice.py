import random

#create function to print results of 2 rolled dice and return their total
def roll_dice():
  min = 1
  max = 6
  d1 = random.randint(min, max)  #get a random dice roll
  d2 = random.randint(min, max)  #get a random dice roll
  print('Roll 1 =', d1 )
  print('Roll 2 =', d2 )
  print('You gain', d1 + d2, 'points!')
  return d1 + d2 