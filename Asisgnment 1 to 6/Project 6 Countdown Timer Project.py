import time

def Countdown_timer():
    seconds = 0
    while True:
        try:
            user_input = int(input("Enter the Countdown Duration in Seconds : "))
            if user_input < 0:
                print("Please Enter a Positive Number.")
                continue
            seconds = user_input
            break
        except ValueError:
            print("Invalid Input. Please Enter a Valid Number.")

    for i in range(seconds, 0, -1):
        print(f"Time Remain : {i} Seconds.", end="\r")
        time.sleep(2)

    print(" Time's Up!  ⏰")  

Countdown_timer()


