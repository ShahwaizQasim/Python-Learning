
# 1. A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user
# for their salary and year of service and print the net bonus amount.

# salary = int(input("Enter your salary: "));
# yearsOfService = int(input("Enter your years of service: "));
# bonus = 0;

# if yearsOfService > 5:
#     bonus = salary * 0.05;
#     print("Your bonus is: ", bonus);
# else :
#     bonus = 0;
#     print("Your bonus is: ", bonus);

# print(bonus)



# 2. Write a program to check whether a person is eligible for voting or not. (accept age from user) if age is
#  greater than 17 eligible otherwise not eligible

# age = int(input("Enter your age: "));

# if age > 17:
#     print("You are eligible for voting");
# else:
#     print("You are not eligible for voting");



# 3. Write a program to check whether a number entered by user is even or odd.

# number = int(input("Enter a number: "));

# if number % 2 == 0: 
#     print("The number is even " + str(number));
# else:
#     print("The number is odd");

# 4. Write a program to check whether a number is divisible by 7 or not. Show Answer

# number =int(input("Enter a number: "));
# if number % 7 == 0:
#     print("The number is divisible by 7");
# else:
#     print("The number is not divisible by 7");



# 5. Write a program to display "Hello" if a number entered by user is a multiple of five , otherwise
# print "Bye".

# userInput = int(input("Enter a number: "));
# if userInput % 5 == 0:
#     print("Hello");
# else:
#     print("Bye");


# 6. Write a program to display the last digit of a number.
number = int(input("Enter a number: "));
lastDigit = number % 10;
print("The last digit of the number is: ", lastDigit);


# 7. A shop will give discount of 10% if the cost of purchased quantity is more than 1000. Ask user for
# quantity Suppose, one unit will cost 100. Judge and print total cost for user.

quantity = int(input("Enter quantity: "))

unit_cost = 100
total_cost = quantity * unit_cost

if total_cost > 1000:
    discount = total_cost * 0.10
    final_cost = total_cost - discount
    print("Discount: ", discount)
    print("Total cost after discount: ", final_cost)
else:
    print("Total cost: ", total_cost)