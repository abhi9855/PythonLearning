s1=float(input("Enter 1st side! : "))
s2=float(input("Enter 2nd side! : "))
s3=float(input("Enter 3rd side! : "))
if s1==s2 and s2==s3:
    print("Equilateral Triangle")
elif s1==s2 or s1==s3 or s2==s3:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")