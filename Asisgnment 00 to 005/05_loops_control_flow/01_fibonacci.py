n = int(input("Enter a Number: "))
x= 0
y = 1
z = 0

while z <= n:
    print(z,end=" ")
    x = y # 1
    y = z # 0
    z = x + y # 1