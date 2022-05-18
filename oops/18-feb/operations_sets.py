st = {1,2,3,4,5,5,5,5,}

print("SET:", st)

print("\nIterating through the set:")
for ele in st:
    print("Ele is:", ele)

length = len(st)
print("\nLength of the set:", length)

element = 2
st.remove(element)
print("\nRemoving an element to the set:", st)

element = 8
st.add(element)
print("\nInserting an element to the set:", st)

st.add(element)
print("\nAdding the same element again to the set:", st)
print("The element will not be repeated")

is_in_set = element in st
print("\nMembership operator:", is_in_set)
if (is_in_set):
    print(f"{element} is in the set - {st}")
else:
    print(f"{element} is not in the set - {st}")

is_in_set = 10 in st
print("\nMembership operator:", is_in_set)
if (is_in_set):
    print(f"10 is in the set - {st}")
else:
    print(f"10 is not in the set - {st}") 

is_contains = st.__contains__(2)
print("\nSet is:", st)
print("Is set contains an element:", is_contains)

st1 = {1,2,3}
st2 = {3,4,5}
print(f"\nst1 : {st1}\nst2 : {st2}")
print("Intersection of sets:", st1.intersection(st2))
print("Difference of sets:", st1 - st2)
