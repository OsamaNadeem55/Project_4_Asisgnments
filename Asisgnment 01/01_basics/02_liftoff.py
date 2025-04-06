import time

def liftoff(start_Value,end_Value,jumped_value):
    for i in range(start_Value,end_Value,-jumped_value):
     time.sleep(1)
    print(i)
       
def main() :

    start_Value = int(input("Enter a Start Value : "))
    end_Value = int(input("Enter a Start Value : "))
    jumped_value = int(input("Enter a Start Value : "))

    liftoff(start_Value,end_Value,jumped_value)
main()