tup = (1, 2, 3, 'rvce', 'mca', 'bca') 

print("\nLength of tuple:", len(tup))

print("\nGetting ith element in tuple:", tup[2])

print("\nReversing tuple:", tup[::-1])

print("\nSlicing tuple:", tup[3:])

print("\nIterating through tuple:")
for ele in tup:
    print("Ele:", ele)

print("\nMembership operator:", "rv" in tup)

tup2 = (11,12,13,14)
print("\nConcatinating tuples:", tup + tup2)

print("\nMax of ele:" , max(tup2))
