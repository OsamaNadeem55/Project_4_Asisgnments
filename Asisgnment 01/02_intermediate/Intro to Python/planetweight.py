def calculate(earth_weight,planet):
     
     if planet == "mercury":
         return earth_weight * 0.376
     
     elif planet == "venus":
         return earth_weight *889
     
     elif planet == "mars":
         return earth_weight *0.378
     
     elif planet == "jupiter":
         return earth_weight *2.36
     
     elif planet == "saturn":
         return earth_weight *1.081
     
     elif planet == "uranus":
         return earth_weight *0.815
     
     elif planet == "neptune":
         return earth_weight *1.14
     
earth_weight = float(input("Enter a Earth Weight : "))
planet = input("Enter a Planet Weight : ").lower()

res = calculate(earth_weight,planet)
print(res)