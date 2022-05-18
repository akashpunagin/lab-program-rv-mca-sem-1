import utils

op1 = utils.Operator()
op2 = utils.Operator()

print("Object 1 initialization:\n")
op1.get()

print("\nObject 2 initialization:\n")
op2.get()

print("\nList 1: ", op1.lst)
print("List 2: ", op2.lst)

print("\nAddition operator overloading")
op1 + op2

print("\nSubstraction operator overloading")
op1 - op2

print("\nMultiplication operator overloading")
op1 * op2

print("\nDivision operator overloading")
op1 // op2

print("\nPower operator overloading")
op1 ** op2
