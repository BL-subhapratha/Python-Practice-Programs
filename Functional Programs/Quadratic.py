import math

a = int(input("Enter the value for a: "))
b = int(input("Enter the value for b: "))
c = int(input("Enter the value for c: "))

print(f"The equation is : {a}*x*x + {b}*x + {c}")

delta =(float)(b*b - 4*a*c)

if delta > 0:
    root1 = (-b + math.sqrt(delta)) / (2*a)
    root2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"The roots of the equation are: {root1} and {root2}.")

elif delta == 0:
    root1 = -b / (2*a)
    print(f"The root of the equation is {root1}.")

else:
    print("No roots for this equation.")