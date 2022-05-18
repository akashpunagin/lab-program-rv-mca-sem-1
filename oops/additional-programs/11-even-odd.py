try:
    num = int(input("Enter a number: "))

    if num % 2 == 0:
        print(f"{num} is even number")
    else:
        print(f"{num} is odd number")
except ValueError as e:
    print("Enter integer value")
except Exception as e:
    print("Error occured")
