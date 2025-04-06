def add_contact(phonebook):
  name = input("Enter Contact Name : ")
  phone = input("Enter Contact Phone Number : ")

  if name in phonebook:
    print(f"{name} is Already in the Phonebook.")
  else:
    phonebook[name] = phone
    print(f"{name} has been Added to the Phonebook.")

def search_contact(phonebook):
  name = input("Enter Contact Name to Search : ")

  if name in phonebook:
    print(f"{name} : {phonebook[name]}")
  else :
    print(f"{name} is Not in the Phonebook.")

def remove_contact(phonebook):
  name = input("Enter Contact Name to Remove : ")

  if name in phonebook:
    del phonebook[name]
    print(f"{name} has been Removed from the Phonebook.")

  else:
    print(f"{name} is Not Found in the Phonebook.")

def display_contact(phonebook):
  print("\n Phone Contact List :")
  for name, number in phonebook.items():
    print(f"{name} : {number}")

  else:
    print("Phonebook is Empty.")




  while True:

    print("\n Phonebook Menu :")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Remove Contact")
    print("4. Display Contact")
    print("5. Exit")

    choice = input("Enter Your Choice (1-5) : ")

    if choice == '1':
      add_contact(phonebook)
    elif choice == '2':
      search_contact(phonebook)
    elif choice == '3':
      remove_contact(phonebook)
    elif choice == '4':
      display_contact(phonebook)
    elif choice == '5':
      print("Exit Phonebook. Goodbye!")

      break

    else:
      print("Invalid Choice. Please  Enter a Number Between 1 to 5.")

phonebook = {}

display_contact(phonebook)