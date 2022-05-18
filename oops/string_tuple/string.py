str1 = "Hello"
str2 = "World"

print("Getting letter in index:", str1[2])

print("\nRepeating string:", str1 * 3)

print("\nSlicing the string", str1[2:])

print("\nReversing string:", str1[::-1])

print("\nCheck if sub string exists in string:", "He" in str1)

print("\nLength of string:", len(str1))

print("\nCount frequencies of letters:", str1.count("l"))

print("\nUppercase:", str1.upper())
print("\nLowercase:", str1.lower())

print("\nIterating through string")
for char in str1:
    print("CHAR:", char)

print("\nConcatinating 2 or more stirng:", str1 + str2)
