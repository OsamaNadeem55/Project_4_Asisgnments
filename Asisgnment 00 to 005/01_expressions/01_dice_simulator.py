import random

num_side = 6

def roll_dice ():
  die1 = random.randint(1, num_side)
  die2 = random.randint(1, num_side)
  total = die1 + die2
  print(f"Total of the Two Dice is {total}")

def main ():
 diel = 10
 print("Diel in main() starts as : " + str (diel))

 roll_dice()
 roll_dice()
 roll_dice()

 print("Diel in main() starts as : " + str (diel))

main()