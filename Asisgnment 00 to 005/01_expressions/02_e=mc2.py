def main() :
  
  c : float = 299792458
  m : float = float(input("Enter Kilo of Mass :  "))

  print("e = m*c^2")
  print("Mass = " + str(m) + " kg")
  print("C = " + str(c) + " m/s")
  print("e = " + str(m*c**2) + " Jules")

main()