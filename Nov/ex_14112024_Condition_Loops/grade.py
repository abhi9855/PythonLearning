
#A: 90-100
#B:80-89
#C:70-79
#D:60-69
#F:0-59

score =int(input("Enter the num! : \n"))
if score>100 or score<0:
    print("You are a SUPERMAN")
elif score>=90 and score<=100:
    print("Your grade is : A")
elif score>=80 and score<=89:
    print("Your grade is : B")
elif score>=70 and score<=79:
    print("Your grade is : C")
elif score>=60 and score<=69:
    print("Your grade is : D")
else:
    print("Your grade is : F")