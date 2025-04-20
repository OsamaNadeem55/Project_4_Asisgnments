import random
import string

def generate_password (name, digit) :

    name = name
    character = string.ascii_letters + string.digits + "!@#$^%&"
    return name[:3] + "".join(random.choice(character) for i in range(digit))

name = input("Enter Your Name : ")
user_input = int(input("Enter the Length of Password : "))

if user_input < 8 :

  print("Password Length Must Be Greater Than 8 Characters.")

else :

  password = generate_password(name,user_input)
  print("Generate Password : ", password)