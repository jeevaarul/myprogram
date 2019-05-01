#Python Program to Solve Quadratic Equation
import cmath
a =input("enter the a value:")
b =input("enter the b value:")
c =input("enter the c value:")

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print(sol1)
print(sol2)