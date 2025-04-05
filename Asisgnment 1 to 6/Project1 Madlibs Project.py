def Madlibs ():


  name = str(input("Enter Your Name "))
  city = str(input("City Name "))
  verb = str(input("Enter Your Verb "))
  animal = str(input("Enter Animal Name "))
  adjective = str(input("Enter Adjective Name "))

  story = f"Ek din, {name} {city} gaya. Wahan usne ek {adjective} {animal} dekha jo {verb} raha tha. Yeh dekh kar, {name} boht hairan hua!"

  print(story)

Madlibs()