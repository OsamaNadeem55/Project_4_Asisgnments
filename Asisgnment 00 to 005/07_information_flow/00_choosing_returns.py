ADULT_AGE = 18

def is_adult(age):

    return age >= ADULT_AGE
age = int(input("How old are You ? "))
print(is_adult(age))