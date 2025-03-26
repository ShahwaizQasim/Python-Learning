# 1) Arithmetic Operators
# Operators jo mathematical operations ke liye use hote hain.

a = 4
b = 5

print("Plus", a + b)
print("Minus", a - b)
print("Multiply", a * b)
print("Exponentiation", a ** b)
print("Divide", a / b)

# 4 ÷ 5 = 0.8, lekin floor division sirf integer part (0) return karega.
print("Floor Division", a//b) # 4 // 5 ka matlab hai 4 ko 5 se divide karo aur integer part return karo.

print("Modulus", a % b)

# Average Three Numbers
a = 4
b = 3
c = 5

print("Average three numbers", (a + b + c) / 3) # BODMAS Rule ki waja se (a + b + c) ko column me rakha hai


# 2) Comparison Operators
# comparison operator values ko compare karne ke liye use hote hain.

num1 = 20
num2 = 30

print(num1 == num2) # False
print(num1 != num2) # False
print(num1 > num2) # False
print(num1 < num2) # False
print(num1 >= num2) # False
print(num1 <= num2) # False


# 3) Logical Operators
# Logical conditions check karne ke liye use hote hain:

x = True
y = False

print(x and y) #false
print(x or y) #true 
print(not y) #true 


# 4) Assignment Operators

c = 9
c += 5
print(c)

d = 15
d *= 2
print(d)


# Examples
# =	a = 5	a = 5
# +=	    a += 3 --> Same --> a = a + 3
# -=	    a -= 2 --> Same --> a = a - 2
# *=	    a *= 4 --> Same --> a = a * 4
# /=	    a /= 2 --> Same --> a = a / 2
# //=	    a //= 3 --> Same --> a = a // 3
# %=	    a %= 2 --> Same --> a = a % 2
# **=	    a **= 2 --> Same --> a = a ** 2