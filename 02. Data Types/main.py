
rating = 4.7 # float 
# print(type (rating))

name = "Shahwaiz" # str
# print(type(name))

marks = 98 # int
# print(type(marks))

is_passed = False # bool
# print(type(is_passed))

my_complex_Number = 4 + 5j # complex
# print(type(my_complex_Number))

fruits_list = ['Apple', 'Mango', 'Banana'] # list
# print(type(fruits_list))

#Isme keys unique hoti hain aur har key ki ek value hoti hai.
user_details = {
    "name" : "Syed Shahwaiz",
    "Roll Number" : 180991,
}
# print(type(user_details)) # dict

detail = (1,2,3)
# print(type(detail)) # tuple


# Python Data Types Test

name = "Shahwaiz" # str
Age = 21  # int
Year_Of_Birth = "12-jan-2005" # str
Is_New_User = True # bool
Fruits = ["Apple", "Mango", "Banana", "WaterMelon"] # list
number = (2,4,6,8) # tuple
trainer_details = {
    "Trainer_Name": "Shehzad Iqbal",
    "Course": "Modern Web And App Development",
    "Duration": "one year",
    "Campus": "Gulshan",
} # dict

print(trainer_details["Trainer_Name"])  # first method
print(trainer_details.get("Trainer_Name")) # second method

name = trainer_details["Trainer_Name"]
course = trainer_details["Course"]

print(f"Trainer Name: {name}")
print(f"course: {course}")


# Python mein f-string (formatted string literal) kehte hain
num = 5
print(f"Double of {num} is {num * 2}")