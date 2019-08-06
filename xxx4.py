import math

x = float(input("mutqagreq x: "))
y = float(input("mutqagreq y: "))

print("f(x,y) = ", (x**2 + (y**2 + 4)*1/3)**1/4 + ((math.fabs(x) + math.fabs(y))**10))