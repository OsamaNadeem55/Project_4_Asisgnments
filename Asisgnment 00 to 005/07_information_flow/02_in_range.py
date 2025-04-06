def is_range(n,low,high):

    if n >= low and n <= high:
        return True
    return False
   
n = int(input("Enter a Number : "))
low = int(input("Enter the Lower Bound : ")) 
high = int(input("Enter the Upper Bound : "))

print(is_range)