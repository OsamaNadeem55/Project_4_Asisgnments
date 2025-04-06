def double(num: int):
    return num * 2


def main():
    num = int(input("Enter a Number : "))
    num_times_2 = double(num)
    print("Double that is", num_times_2)


main()