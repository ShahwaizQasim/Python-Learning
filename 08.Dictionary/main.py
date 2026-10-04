# Dictionary key value pairs me data ko store karta hai
# Dictionary key always string 

user = {
    "name": "Sarah",
    "plan": "Pro",
    "active": True,
    "storage_gb": 250,
    "marks": [10,20,60,80]
}

# access values by key, not by index
print(user["name"])
print(user["marks"])
print(user["active"])


# "age" isn't a key in user -- direct [] access raises KeyError for a missing key
# print(user["age"])


# get function
print(user.get("age", "N/A"))
print(user.get("marks", "no marks"))


# key ki value update 
user["name"] = "Ahad"
print(user)

user["active"] = False;
print(user)

print(user)

# dictionary ki key value delete karne ka function pop() hai
# removedKey = user.pop('marks')
# print(removedKey)

# print(user)


# del user["storage_gb"]
# print(user)


# dictionary ki all keys ayengi 
print(user.keys());

# dictionary ki all values ayengi 
print(user.values());

print(user.items()); # dictionary ki all key value pairs ayengi