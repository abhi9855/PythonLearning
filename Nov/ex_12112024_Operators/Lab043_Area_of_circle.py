#write a program to calculate the
#area of circle given its radius using the formula
#area=3.14*r*r

#logic building formula
#step1=figure out i/p,o/p
#input =r , data type =float
#pi=3.14
#power=pow or ** -->any
#o/p=float-area, print area

#step2 = rought logic
#area=3.14*pow(r,2)

#step3
try:
    radius=float(input("Enter the radius to find the area of circle : "))
    area = 3.14 * (radius * radius)

    print(f"Area of Circle whose radius is {radius} : {area}")
except ValueError:
    print("Error: Cannot give radius as String. It should be an Integer ")


#*->mul
#** -> power
import math
print(math.pi)
print(math.pow(radius,2))
area=math.pi * math.pow(radius,2)
print("area of circle is ->",area)

import math
print(math.pi)
print(math.pow(2,2))
print(math.sin(90))
print(math.cos(90))
print(math.tan(90))