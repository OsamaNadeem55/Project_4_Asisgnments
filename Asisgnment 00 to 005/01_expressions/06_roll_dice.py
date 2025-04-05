import random

def dice () :
  
  die1 : int = random.randint(1,6)
  die2 : int = random.randint(1,6)
  total : int = int(die1 + die2)

  print("First Die : " + str(die1))
  print("Second Die : " + str(die2))
  print(f"Total of Two Dice : {total}")

dice()