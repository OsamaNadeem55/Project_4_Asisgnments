Max_length : int = 3

def shorter (list) :
  while len(list) > Max_length :
    last_element = list.pop()
    print(last_element)

def get_list() :
  list = []
  element = input("Enter an Element to Add to the List : ")
  while element != "":
    list.append(element)
    element = input("Enter an Element to Add to the List : ")
  return list

def main() :
  list = get_list()
  shorter(list)

main()