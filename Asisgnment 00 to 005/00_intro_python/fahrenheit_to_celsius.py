def main():
  try:

    fahrenheit = int(input("Enter the Temperature in Fahrenheit: "))

    celsius = (fahrenheit - 32) * 5.0/9.0
    print(f" Temperature {fahrenheit} F = {celsius} C")
  except ValueError:
    print("Invalid Input!")

main()