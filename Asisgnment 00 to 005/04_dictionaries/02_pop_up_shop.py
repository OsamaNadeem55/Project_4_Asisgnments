def calculate_total_cost():
    fruit_price = {

        "apple": 5.00,
        "banana": 6.50,
        "orange": 4.75,
        "grape": 10.2,
        "kiwi": 12.5
    }

    total_cost = 0

    for fruit, price in fruit_price.items():
        while True:
            try:
                quantity = int(input(f"How many {fruit} Do You Want ? "))
                if quantity < 0:
                    print("Invalid input. Please enter a Positive Number.")
                    continue
                total_cost += price * quantity
                break
            except ValueError:
                print("Invalid input. Please Enter a Valid Number.")

    print(f"\n Your Total Cost is : ${total_cost:.2f}")

calculate_total_cost()