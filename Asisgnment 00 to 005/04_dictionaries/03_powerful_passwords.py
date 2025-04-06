import hashlib

def hash_password(password):
  return hashlib.sha256(password.encode()).hexdigest()
  

stored_login = {
    "user@example" : hash_password("555"),
    "admin2@example" : hash_password("adminpass")
}

def login(email,password) :
  if email in stored_login :
    return stored_login[email] == hash_password(password)
    return False


email = input("Enter Your Email : ")
password = input("Enter Your Password : ")

if login(email,password):
  print("Login Successful.")
else:
  print("Invalid Credentials.")