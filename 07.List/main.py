fruitList = ['Mango', 'Apple', 'Melon', 'WaterMelon'];
print(fruitList) # Mango

StudentNames = ["Ali", "Shahwaiz", "Wasid", "Junaid","Ahsan"]

print(StudentNames) # ['Ali', 'Shahwaiz', 'Wasid', 'Junaid', 'Ahsan']
print(StudentNames[0]) # Ali

print(StudentNames[-1]) # list last value print 

print(len(StudentNames)) # list length print

# append()
StudentNames.append("Qasim Boss"); # list kay end me value add karta hai
print(StudentNames)

# pop()
StudentNames.pop(); # list kay end me value remove karta hai
print(StudentNames)

StudentNames.pop(3);
print(StudentNames) # list me se junaid remove ho gaya

StudentNames.index("Ali")
print(StudentNames.index("Wasid")) # list me elements ka index confirm karne ka function

# Insert
StudentNames.insert(0, "Qasim Ali"); # list me index 0 pr new value add karne ka function
print(StudentNames) # ['Qasim Ali', 'Ali', 'Shahwaiz', 'Wasid', 'Ahsan']


# Remove 
city = ["Karachi", "Islamabad", "Hyderabad", "Rawalpindi","Lahore","Islamabad"];
city.remove("Islamabad") # remove list me se value ko remove karta hai
city.remove("Islamabad")
print(city)


# extend
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars) # extend multiple elements ko add karta hai list me

print(fruits)

marks = [50, 22,90,76,97];

print(max(marks)) # 97
print(min(marks)) # 22
print(sum(marks)) # 335


# Nested list 
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# print(matrix[0])
# print(matrix[1])
# print(matrix[2])

print(matrix[0][1]) # 2
print(matrix[0][2]) # 3

print(matrix[1][1]) # 5
print(matrix[2][2]) # 9


# Tuples 
# Why we use tuples ?
# aesi values jo hum change nahi karna chaty wo values tuples me rakhty hain like CNIC, Date of Birth ye change
# nahi ho sakhta aesi values hum tuple me rakh sakhty hain

saylani_campuses = ('Malir-campus', 'Z.A', 'lahore-campus', 'Headoffice', 'Ibne-Adam');
print(saylani_campuses)