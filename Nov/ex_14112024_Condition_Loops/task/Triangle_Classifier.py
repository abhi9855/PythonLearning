# Triangle Classifier:

# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.

def classify_triangle(s1, s2, s3):
    if s1 and s2 and s3 > 0:
        if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
            if s1 == s2 == s3:
                return "Equilateral"
            elif s1==s2 or s1==s3 or s2==s3:
                return "Isosceles"
            else:
                return "Scalene"
        else:
            print("Not a Triangle")
    else:
        print("Enter a valid integer")

side1=float(input("Enter 1st side! : "))
side2=float(input("Enter 2nd side! : "))
side3=float(input("Enter 3rd side! : "))

result=classify_triangle(side1, side2, side3)
print(f"The triangle is classified as : {result}")