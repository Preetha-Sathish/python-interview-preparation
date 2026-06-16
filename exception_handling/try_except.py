try:
    num=int(input("Enter a number: "))
    print(100/num)
except ZeroDivisionError:
    print("Cannot Divide by zero")
except ValueError:
    print("Please enter a valid number")
