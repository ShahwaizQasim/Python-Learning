# python first program run
print("hello world")


age = 22
print("age=>", age)

name = "Shahwaiz Qasim"
print("MyName", name)


# valid identifiers
age = 24
first_name = "Syed Shahwaiz"
_id = 10243
name2 = "Muhammad Ali"

# Invalid Identifiers 
'''
class = "ali"
2name = "wasid"
mark$ = 22
my name = "shahwaiz"
my-name = "ali"
'''

# 1)Print Your Name with your Father name and Date of birth using suitable escape sequence charactor
name = "Syed Shahwaiz"
FatherName = "Qasim Ali"
DateOfBirth = "10-Aug-2003"
age= 23;

print(f"My name is {name}\n my father name is {FatherName}\n my age is {age}\n my date of birth is {DateOfBirth}\n")


# 2) Write your small bio using variables and print it using print function
name = "Ali Khan"
profession = "Software Engineer"
experience = "5 years"
hobby = "reading tech blogs and contributing to open-source projects"

print(f"Hello, my name is {name}. I am a {profession}.")
print(f"I have been working in software development for over {experience}.")
print(f"In my free time, I enjoy {hobby}.")

# variables swapping 
a = 10;
b = 20;

a = a + b  # 30
b = a - b  # 10
a = a - b 

print( f"After swapping: a = {a}, b = {b}")


# Q) Take the price of an item and a discount percentage in variables, then calculate and print the discount 
# amount and the final price after discount

discount = 10
price = 1000
discount_Amount = (discount * price) / 100
final_price = price - discount_Amount

print("discount_Amount==> ", discount_Amount)
print("final_price==> ", final_price)