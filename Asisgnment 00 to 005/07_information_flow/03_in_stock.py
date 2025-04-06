def num_in_stock(fruit):
    inventry = {
        'apples': 5,
        'bananas': 0,
        'oranges': 2,
        'pears': 0,
        'grapes': 0,
        'kiwi': 0,
    }
    return inventry.get(fruit,0)
    
def main():

    fruit = input("Enter the Name of the Fruit : ").lower()
    stock = num_in_stock(fruit)
    if stock > 0 :
        print(f"{fruit.capitalize()} are in Stock. We have {stock} in Stock.")
    else:
        print(f"{fruit.capitalize()} are not in Stock. We have {stock} in Stock.")
        
main()