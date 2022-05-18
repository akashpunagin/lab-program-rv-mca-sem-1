lst = [1,2,3,4,5,6]

print("LIST:", lst)

print("\nAccessing an element from list:", lst[2])

print("\nSlicing a list:", lst[2:5])

element = 7
lst.append(element)
print("\nAppending element to the list:", lst)

popped_element = lst.pop()
print("\nPopping an element from the list:", lst)
print("Popped element:", popped_element)

length = len(lst)
print("\nLength of the list:", length)

print("Iterating through the list:")
for ele in lst:
    print("Ele is:", ele)

lst.append(2)
freq = lst.count(2)
print("\nAppending 2 in the list, lst is:", lst)
print("\nCount occurance in the list:", freq)

reverse = lst[::-1]
print("Reversing the list:", reverse)

