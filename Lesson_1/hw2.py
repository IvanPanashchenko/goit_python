import math
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

D = b**2-4*a*c

if D < 0:
    print ("Нет решения")
elif D == 0:
    x = (-b+math.sqrt(b**2-4*a*c))/2*a
    print ("Только одно решение: "), x
else:
    x1 = (-b+math.sqrt((b**2)-(4*(a*c))))/(2*a)
    x2 = (-b-math.sqrt((b**2)-(4*(a*c))))/(2*a)
    print ( x1 , "и", x2)