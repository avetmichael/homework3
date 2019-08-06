import math

x = float(input("mutqagreq x: "))
y = float(input("mutqagreq y: "))

print("f(x,y) = ", math.atan(math.fabs(x**2 - y)/(x**2 + y**2)) + math.log10(x**2 + 1))