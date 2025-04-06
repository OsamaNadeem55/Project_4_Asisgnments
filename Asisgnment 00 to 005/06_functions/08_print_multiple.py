def print_multiple(message, times):

    for i in range(times):
        print(message)

def main():
    
    msg = input("Enter a Message: ")
    times = int(input("How Many Times Do You Want to Print It ? "))
    print_multiple(msg, times)
    
main()