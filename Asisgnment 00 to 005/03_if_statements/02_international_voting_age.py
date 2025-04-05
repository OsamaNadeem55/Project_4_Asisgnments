Lahore : int = 16
Karachi : int = 25
Islamabad : int = 48

age : int = int(input("Enter Your Age : "))

def main() :
  if age >= Lahore :
    print(f"Your Age is {age}. You are Eligible to Vote in Lahore !")
  else :
    print(f"Your Age is {age}. You are not Eligible to Vote in Lahore !")

  if age >= Karachi :
    print(f"Your Age is {age}. You are Eligible to Vote in Karachi !")
  else :
    print(f"Your Age is {age}. You are not Eligible to Vote in Karachi !")

  
  if age >= Islamabad :
    print(f"Your Age is {age}. You are Eligible to Vote in Islamabad !")
  else :
    print(f"Your Age is {age}. You are not Eligible to Vote in Islamabad !")

main()