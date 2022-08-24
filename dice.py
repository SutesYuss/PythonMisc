"""Author: Sudi Yussuf
"""

import random

def diceroller(sides=6, samples=10000):
  die = random.randint(1,6)
  counts = {}
  for i in range(samples):
        roll = random.randint(1,6)
        if roll not in counts:
            counts[roll] = 0
        counts[roll] += 1
  return (counts)

# m = diceroller()

def print_bar_chart(dict):
  print("Rolls of Each Dice Value")
  print()
  k = list(dict.keys())
  k.sort()
  bar = "\u2588"
  stringTest = ""
  colon = " : "
  for i in k:
    j  = dict[i]//15
    print(str(i) + colon + (bar * j))
    print()


# print_bar_chart(m)