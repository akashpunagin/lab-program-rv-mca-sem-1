dct = {
    "name": "Raju",
    "age": 21,
}

print("Dictionary is:", dct)

user_key = input("Enter key to check: ")

if user_key in dct.keys():
    print("Key exists")
else:
    print("Key does not exists")
