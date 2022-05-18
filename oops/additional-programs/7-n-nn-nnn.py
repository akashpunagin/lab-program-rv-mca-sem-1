try:
    n = int(input("Enter n: "))
    print("Result:", n + (n*n) + (n*n*n))
except ValueError as e:
    print("Enter integer value")
except Exception as e:
    print("Error")
