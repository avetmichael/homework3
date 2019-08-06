import math

a = float(input("mutqagreq a: "))
b = float(input("mutqagreq b: "))
c = float(input("mutqagreq c: "))

diskriminant = b**2 - 4*a*c

if diskriminant > 0:
    print("uni 2 lutsum")

elif diskriminant == 0:
    print("uni mek lutsum")

else:
    print("lutsum chuni")


