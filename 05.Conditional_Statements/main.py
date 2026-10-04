# if else syntax
# if condition:
#     print()
# else:
#     print()


age = 12
if age > 18:
    print("you can vote")
else:
    print("you can not vote")

print("This will always be execute")


# if elif else syntax 

# if / elif / else -- runs one block based on which condition is True

# syntax:
# if condition:
#     logic
# elif another_condition:
#     logic
# else:
#     logic

num = 0

if num > 0:
    print("Positive Number")
elif num == 0:
    print("Zero")
else:
    print("Negative Number")


userName = "Shahwaizd"
if userName == "Shahwaiz":
    print("condition true")
else:
    print("condition false")


age = 15;
userAge = int(input("Enter Your Age: "));

if userAge > age and userAge < 30:
    print("You are eligible for this job")
else:
    print("You are not eligible for this job")



# Marks grading:
# 90+     -> A+
# 80-89   -> A
# 70-79   -> B
# 50-69   -> C
# below 50 -> Failed

# marks = int(input("Enter your marks..."))
# print(marks)

marks = 90

if marks >= 90: # grade A+
    print("You got grade A+ Congratulations!")

elif marks >= 80 and marks < 90: # grade A
    print("You got grade A+ Congratulations!") 

elif marks >= 70 and marks < 80: # grade B
    print("Grade B.. Keep it up!") 

elif marks >= 50 and marks < 70: # grade C
    print("grade C ... do hard work")

else: # anything below 50
    print("Failed ... retry")



numbers = [1,2,3,4,5,6,7] 
num = int(input("Enter a number... "))

# in -- checks whether num exists anywhere in the list
if num in numbers:
    print("yes")
else:
    print("no")