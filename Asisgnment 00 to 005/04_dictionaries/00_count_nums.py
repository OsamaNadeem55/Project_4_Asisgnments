def count_numbers() :
  count_dic = {}

  while True:
    num = input("Enter a number (or 'Exit' to stop) : ")
    if num.lower() == 'Exit':
      break
    if num.isdigit():
      num = int(num)
      count_dic[num] = count_dic.get(num, 0) + 1
    else:
      print("Invalid input. Please Enter a Number or 'Exit'.")
      return count_dic

def display_counts(count_dic):
  print("\n Number Counts:")
  for key, value in count_dic.items():
    print(f"{key} Appears {value} Times ")

count_dic = count_numbers()
display_counts(count_dic)