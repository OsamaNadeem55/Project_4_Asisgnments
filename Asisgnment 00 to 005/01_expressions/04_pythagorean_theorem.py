def remainder() :
  
  num1 : int = int(input("Enter an Integer to be Divided :  "))
  num2 : int = int(input("Enter an Integer to Divided by :  "))
  
  quotient : int = num1 // num2
  remainder : int = num1 % num2

  print(f"The Result of Following Division is {quotient} with the Reminder of {remainder}")

remainder()