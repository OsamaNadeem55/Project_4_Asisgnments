def main() :

  list = []
  value = input("Enter a Value to Add to the List : ")

  while value :
    list.append(value)
    value = input("Enter a Value to Add to the List : ")
  print("Here is the List : ",list)
  
main()