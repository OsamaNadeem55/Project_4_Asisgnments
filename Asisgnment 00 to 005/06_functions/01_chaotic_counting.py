import random

DONE_LIKELIHOOD = 0.3

def Done():
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    for i in range(1, 10):
        if Done():
           return
        print(i,end=" ")
def main():
        print("I'm Going to Count till 10 or until I Feel Like Stop, which were Comes First.")
        chaotic_counting()
        print("\n I'm Done.")
main()