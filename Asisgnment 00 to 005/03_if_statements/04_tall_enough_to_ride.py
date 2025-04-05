min_height : int = 50

def main() :
  
  user : int = int(input("How Tall are You ? : "))
  if user >= min_height :
    print(f"Your Height is {user}. You are Eligible to Ride !")
  else :
    print(f"Your Height is {user}. You are not Enough to Ride. May be Next Year ")

main()