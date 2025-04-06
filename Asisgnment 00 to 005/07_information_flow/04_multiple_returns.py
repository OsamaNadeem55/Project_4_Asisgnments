def get_user_data():

    first_name = input("Enter Your First Name : ")
    last_name = input("Enter Your Last Name : ")
    email = input("Enter your Email Address : ")

    return first_name, last_name, email

print("Please Enter Your Details :")

user_data = get_user_data()
print("Received the Following User Data : ", user_data)