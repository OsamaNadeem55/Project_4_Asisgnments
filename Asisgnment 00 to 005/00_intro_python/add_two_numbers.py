def main():
 try:

   num1 = (input("Enter the First Number: "))
   num1 = int(num1)

   num2 = (input("Enter the Second Number: "))
   num2 = int(num2)

   total = num1 + num2
   print(f"{num1} + {num2} = {total}")

 except ValueError:
  print("Invalid Input! Please Enter Number Only")

main()