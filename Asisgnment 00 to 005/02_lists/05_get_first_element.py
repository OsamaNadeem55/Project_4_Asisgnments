def get_first_element(list) :
  print(list[0])

def get_list() :
  
  list = []
  element : str = input("Enter an Element to Add to the List : ")
  while element != "":
    list.append(element)
    return list

def main() :
  
  list = get_list()
  get_first_element(list)

main()